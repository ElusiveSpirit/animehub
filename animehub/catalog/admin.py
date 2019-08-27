from django.contrib import admin

from animehub.catalog.models import Anime, Genre, Studio


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    pass


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    pass
