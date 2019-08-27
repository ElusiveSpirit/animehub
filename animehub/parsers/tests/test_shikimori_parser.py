import ujson

from unittest.mock import patch

from django.test import TestCase

from animehub.catalog.models import Anime, Genre, Studio, Image
from animehub.parsers.shikimori import ShikimoriParser, ShikimoriClient


class ShikimoriParserTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ShikimoriParserTest, cls).setUpClass()
        with open('./animehub/parsers/tests/mocks/anime_dr_stone.json', 'br') as f:
            cls.mock_anime_dr_stop = ujson.loads(f.read().decode('utf-8'))

    def setUp(self) -> None:
        client = ShikimoriClient()
        self.parser = ShikimoriParser(client)

    @patch('animehub.parsers.shikimori.ShikimoriClient.fetch_by_id')
    def test_save_by_id(self, fetch_by_id):
        fetch_by_id.return_value = self.mock_anime_dr_stop
        anime = self.parser.save_by_id(38691)
        self.assertEqual(Anime.objects.count(), 1)
        self.assertEqual(Genre.objects.count(), 3)
        self.assertEqual(Studio.objects.count(), 1)
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(anime.title, 'Доктор Стоун')
        self.assertEqual(anime.genres.count(), 3)
        self.assertEqual(anime.studios.count(), 1)

    @patch('animehub.parsers.shikimori.ShikimoriClient.fetch_by_id')
    def test_save_by_id_updates_object(self, fetch_by_id):
        fetch_by_id.return_value = self.mock_anime_dr_stop
        self.parser.save_by_id(38691)
        anime = self.parser.save_by_id(38691)
        self.assertEqual(Anime.objects.count(), 1)
        self.assertEqual(Genre.objects.count(), 3)
        self.assertEqual(Studio.objects.count(), 1)
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(anime.title, 'Доктор Стоун')
