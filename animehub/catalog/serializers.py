from rest_framework.serializers import ModelSerializer

from animehub.catalog.models import Anime, Genre, Studio, Image


class StudioSerializer(ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ('link', )


class AnimeSerializer(ModelSerializer):
    image = ImageSerializer(read_only=True)
    studios = StudioSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Anime
        fields = '__all__'
