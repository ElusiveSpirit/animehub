from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from animehub.catalog.models import Anime, Genre, Studio, Image, Video, VideoSource


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
        fields = ('link',)


class AnimeSerializer(ModelSerializer):
    image = ImageSerializer(read_only=True)
    studios = StudioSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Anime
        fields = '__all__'


class VideoSourceWithVideo(ModelSerializer):
    class Meta:
        model = VideoSource
        fields = ('video_id', 'number', 'id', 'translation_type')


class AnimeDetailSerializer(ModelSerializer):
    image = ImageSerializer(read_only=True)
    studios = StudioSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    first_video_source = VideoSourceWithVideo(read_only=True)

    class Meta:
        model = Anime
        fields = '__all__'


class VideoSourceSerializer(ModelSerializer):
    source_name = SlugRelatedField(slug_field='name', read_only=True)
    prev_video = VideoSourceWithVideo(read_only=True)
    next_video = VideoSourceWithVideo(read_only=True)

    class Meta:
        model = VideoSource
        fields = ('id', 'source_name', 'team_name', 'people_list', 'translation_type', 'embed_link',
                  'prev_video', 'next_video')


class VideoSourceMinSerializer(ModelSerializer):
    source_name = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = VideoSource
        fields = ('id', 'source_name', 'team_name', 'people_list', 'translation_type')


class VideoSerializer(ModelSerializer):
    sources = VideoSourceMinSerializer(many=True, source='videosource_set', read_only=True)

    class Meta:
        model = Video
        fields = ('id', 'type', 'number', 'sources')
