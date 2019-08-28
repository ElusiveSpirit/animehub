from typing import Optional

from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse


class Studio(models.Model):
    name = models.CharField(max_length=128, unique=True)
    filtered_name = models.CharField(max_length=128, blank=True, null=True)
    real = models.BooleanField(default=True)
    image = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)
    russian = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Image(models.Model):
    link = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.link


class AnimeManager(models.Manager):
    def active(self):
        return self.filter(is_deleted=False) \
            .order_by('-updated_at') \
            .prefetch_related('genres', 'studios') \
            .select_related('image')


class Anime(models.Model):
    TYPE_TV = 'tv'
    TYPE_OVA = 'ova'
    TYPE_ONA = 'ona'
    TYPE_FILM = 'film'
    TYPE_PREVIEW = 'preview'
    TYPE_SPECIAL = 'special'
    TYPE_OPENING = 'open'
    TYPE_ENDING = 'end'
    TYPE_MENU = 'menu'
    TYPE_BONUS = 'bonus'
    TYPE_OTHER = 'other'
    TYPE_CHOICES = (
        (TYPE_TV, 'TV'),
        (TYPE_OVA, 'OVA'),
        (TYPE_ONA, 'ONA'),
        (TYPE_FILM, 'Фильм'),
        (TYPE_PREVIEW, 'Preview'),
        (TYPE_SPECIAL, 'Special'),
        (TYPE_OPENING, 'Opening'),
        (TYPE_ENDING, 'Ending'),
        (TYPE_MENU, 'Menu'),
        (TYPE_BONUS, 'Бонус'),
        (TYPE_OTHER, 'Другой'),
    )
    shikimori_id = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=400)
    title_latin = models.CharField(max_length=400, blank=True, null=True)
    slug = models.SlugField(max_length=400, blank=True)
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.SET_NULL)

    description = models.TextField(blank=True, null=True)

    score = models.CharField(max_length=10, blank=True, null=True)
    kind = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    duration = models.PositiveSmallIntegerField(blank=True, null=True)
    episodes = models.PositiveSmallIntegerField(blank=True, null=True)
    episodes_aired = models.PositiveSmallIntegerField(blank=True, null=True)

    aired_on = models.DateField(blank=True, null=True)
    released_on = models.DateField(blank=True, null=True)

    rating = models.CharField(max_length=10)

    english_titles = ArrayField(models.CharField(max_length=400), blank=True)
    japanese_titles = ArrayField(models.CharField(max_length=400), blank=True)
    other_titles = ArrayField(models.CharField(max_length=400), blank=True)

    next_episode_at = models.DateTimeField(blank=True, null=True)

    genres = models.ManyToManyField(Genre)
    studios = models.ManyToManyField(Studio)

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AnimeManager()

    @property
    def first_video_source(self) -> Optional['VideoSource']:
        video = self.video_set.first()
        return video.videosource_set.first() if video else None

    def __str__(self) -> str:
        return self.title


class VideoSourceName(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Источник видео'
        verbose_name_plural = 'Источники видео'


class VideoManager(models.Manager):
    def active(self):
        return self.filter(is_deleted=False)


class Video(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.SET_NULL, null=True)

    type = models.CharField('Тип серии', max_length=20, blank=True, null=True, choices=Anime.TYPE_CHOICES)
    number = models.PositiveIntegerField('Номер серии', default=0, blank=False, null=False)

    admin_order = models.PositiveIntegerField('Сортировка', default=0, blank=False, null=False)

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = VideoManager()

    @property
    def prev_video(self) -> Optional['Video']:
        if self.number > 0:
            return Video.objects.filter(number=self.number - 1).first()

    @property
    def next_video(self) -> Optional['Video']:
        return Video.objects.filter(number=self.number + 1).first()

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse(f'admin:{content_type.app_label}_{content_type.model}_change', args=(self.id,))

    def __str__(self) -> str:
        return f'{self.anime}: {self.type} {self.number}'

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        ordering = ['admin_order']


class VideoSourceManager(models.Manager):
    def active(self):
        return self.filter(is_deleted=False)


class VideoSource(models.Model):
    TRANSLATION_RU_VOICE = 'ru-voice'
    TRANSLATION_RU_SUB = 'ru-sub'
    TRANSLATION_EN_VOICE = 'en-voice'
    TRANSLATION_EN_SUB = 'en-sub'
    TRANSLATION_JP_SUB = 'jp-sub'
    TRANSLATION_RAW = 'raw'
    TRANSLATION_CHOICES = (
        (TRANSLATION_RU_VOICE, 'Озвучка'),
        (TRANSLATION_RU_SUB, 'Русские субтитры'),
        (TRANSLATION_EN_VOICE, 'Английская озвучка'),
        (TRANSLATION_EN_SUB, 'Английские субтитры'),
        (TRANSLATION_JP_SUB, 'Японские субтитры'),
        (TRANSLATION_RAW, 'RAW'),
    )

    video = models.ForeignKey(Video, verbose_name='Видео', on_delete=models.CASCADE)

    embed_link = models.CharField('Ссылка', max_length=1000, null=True)

    source_name = models.ForeignKey(VideoSourceName, verbose_name='Источник', on_delete=models.SET_NULL, null=True)
    team_name = models.CharField('Название команды', max_length=120, null=True)
    people_list = models.CharField('Список людей', max_length=240, blank=True, null=True)

    translation_type = models.CharField('Тип перевода', max_length=20, blank=True, null=True,
                                        choices=TRANSLATION_CHOICES)

    admin_order = models.PositiveIntegerField('Сортировка', default=0, blank=False, null=False)

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = VideoSourceManager()

    @property
    def number(self):
        return self.video.number

    @property
    def prev_video(self) -> Optional['VideoSource']:
        video = self.video.prev_video
        return self._choose_video_source_close_to_current(video) if video else None

    @property
    def next_video(self) -> Optional['VideoSource']:
        video = self.video.next_video
        return self._choose_video_source_close_to_current(video) if video else None

    def _choose_video_source_close_to_current(self, video: Video) -> 'VideoSource':
        """Подобрать видео источник приближенный к текущему"""
        same_translation_source_team_video_src = video.videosource_set.filter(
            translation_type=self.translation_type,
            source_name=self.source_name,
            team_name=self.team_name
        ).first()

        if same_translation_source_team_video_src:
            return same_translation_source_team_video_src

        same_translation_video_src = video.videosource_set.filter(
            translation_type=self.translation_type,
        ).first()

        if same_translation_video_src:
            return same_translation_video_src

        return video.videosource_set.all().first()

    def __str__(self) -> str:
        return f'{self.video}: {self.translation_type}'

    class Meta:
        verbose_name = 'Видео файл'
        verbose_name_plural = 'Видео файлы'
        ordering = ['admin_order']
