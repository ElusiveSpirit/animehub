import logging

import requests
from typing import List, Dict, Any, Optional

from slugify import slugify

from animehub.catalog.models import Anime, Genre, Studio, Image

logger = logging.getLogger(__name__)


class ShikimoriClient:
    BASE_URL = 'http://shikimori.one/api'
    BASE_HEADERS = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.100 Safari/537.36',
    }

    def __init__(self) -> None:
        pass

    def fetch_list(self, *, page: int = 1, limit: int = 20, **kwargs) -> List[Dict[str, Any]]:
        resp = requests.get(
            f'{self.BASE_URL}/animes',
            params={
                'page': page,
                'limit': limit,
                **kwargs,
            },
            headers=self.BASE_HEADERS,
        )
        resp.raise_for_status()
        return resp.json()

    def fetch_by_id(self, anime_id: int) -> Dict[str, Any]:
        resp = requests.get(f'{self.BASE_URL}/animes/{anime_id}', headers=self.BASE_HEADERS)
        resp.raise_for_status()
        return resp.json()


class ShikimoriParser:
    def __init__(self, client: ShikimoriClient) -> None:
        self._client = client

    @staticmethod
    def save_genre(genre_data: Dict[str, Any]) -> Optional[Genre]:
        try:
            obj, _ = Genre.objects.update_or_create(
                name=genre_data['name'],
                defaults={'russian': genre_data.get('russian')}
            )
            return obj
        except KeyError:
            logger.warning(f'Genre does not have name field {genre_data}')

    @staticmethod
    def save_studio(studio_data: Dict[str, Any]) -> Optional[Studio]:
        try:
            obj, _ = Studio.objects.update_or_create(
                name=studio_data['name'],
                defaults={
                    'filtered_name': studio_data.get('filtered_name'),
                    'real': studio_data.get('real', True),
                    'image': studio_data.get('image'),
                }
            )
            return obj
        except KeyError:
            logger.warning(f'Studio does not have name field {studio_data}')

    def save_by_id(self, anime_id: int) -> Anime:
        data = self._client.fetch_by_id(anime_id)

        genres = data.get('genres', [])
        genres_list = []
        for genre in genres:
            obj = self.save_genre(genre)
            if obj:
                genres_list.append(obj)

        studios = data.get('studios', [])
        studios_list = []
        for studio in studios:
            obj = self.save_studio(studio)
            if obj:
                studios_list.append(obj)

        if 'image' in data:
            image, _ = Image.objects.get_or_create(link=data['image']['original'])
        else:
            image = None

        anime_obj, _ = Anime.objects.update_or_create(
            shikimori_id=data['id'],
            defaults=dict(
                title=data['russian'],
                title_latin=data['name'],
                slug=slugify(data['russian']),
                image=image,
                description=data['description'],
                score=data['score'],
                kind=data['kind'],
                status=data['status'],
                duration=data['duration'],
                episodes=data['episodes'],
                episodes_aired=data['episodes_aired'],
                aired_on=data['aired_on'],
                released_on=data['released_on'],
                rating=data['rating'],
                english_titles=[title for title in data['english'] if title],
                japanese_titles=[title for title in data['japanese'] if title],
                other_titles=[title for title in data['synonyms'] if title],
                next_episode_at=data['next_episode_at'],
            )
        )
        anime_obj.genres.set(genres_list)
        anime_obj.studios.set(studios_list)
        return anime_obj
