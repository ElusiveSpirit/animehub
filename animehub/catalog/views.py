from rest_framework.generics import ListAPIView, RetrieveAPIView

from animehub.catalog.models import Anime
from animehub.catalog.serializers import AnimeSerializer


class AnimeListView(ListAPIView):
    queryset = Anime.objects\
        .order_by('-updated_at')\
        .prefetch_related('genres', 'studios')\
        .select_related('image')
    serializer_class = AnimeSerializer


class AnimeRetrieveView(RetrieveAPIView):
    queryset = Anime.objects\
        .prefetch_related('genres', 'studios')\
        .select_related('image')
    serializer_class = AnimeSerializer
    lookup_field = 'slug'
