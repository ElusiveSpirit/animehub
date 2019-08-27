from django.contrib.postgres.fields import ArrayField
from django.db import models


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


class Anime(models.Model):
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

    english_titles = ArrayField(models.CharField(max_length=400))
    japanese_titles = ArrayField(models.CharField(max_length=400))
    other_titles = ArrayField(models.CharField(max_length=400))

    next_episode_at = models.DateTimeField(blank=True, null=True)

    genres = models.ManyToManyField(Genre)
    studios = models.ManyToManyField(Studio)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
