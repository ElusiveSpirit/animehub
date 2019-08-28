from rest_framework.generics import ListAPIView, RetrieveAPIView

from animehub.catalog.models import Anime, Video, VideoSource
from animehub.catalog.serializers import AnimeSerializer, AnimeDetailSerializer, VideoSerializer, VideoSourceSerializer


class AnimeListView(ListAPIView):
    queryset = Anime.objects.active()
    serializer_class = AnimeSerializer


class AnimeRetrieveView(RetrieveAPIView):
    queryset = Anime.objects.active()
    serializer_class = AnimeDetailSerializer
    lookup_field = 'slug'


class VideoRetrieveView(RetrieveAPIView):
    queryset = Video.objects.active()
    serializer_class = VideoSerializer


class VideoSourceRetrieveView(RetrieveAPIView):
    queryset = VideoSource.objects.active()
    serializer_class = VideoSourceSerializer
