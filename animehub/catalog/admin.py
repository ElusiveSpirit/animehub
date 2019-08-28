from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from animehub.catalog.models import Anime, Genre, Studio, Video, VideoSource, VideoSourceName


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    pass


class VideoSourceInline(SortableInlineAdminMixin, admin.TabularInline):
    model = VideoSource


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoSourceInline]


@admin.register(VideoSourceName)
class VideoSourceNameAdmin(admin.ModelAdmin):
    pass


@admin.register(VideoSource)
class VideoSourceAdmin(admin.ModelAdmin):
    pass


class StudioInline(admin.TabularInline):
    model = Anime.studios.through


class GenreInline(admin.TabularInline):
    model = Anime.genres.through


class VideoInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Video
    fields = ('type', 'number', 'is_deleted', '_get_edit_btn')
    readonly_fields = ('_get_edit_btn',)

    def _get_edit_btn(self, obj):
        return mark_safe(f'<a href="{obj.get_admin_url()}" class="changelink" target="_blank">Изменить</a>')


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    inlines = [VideoInline]
