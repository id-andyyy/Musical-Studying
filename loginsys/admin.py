from django.contrib import admin

from .models import Profiles, Levels, Genres, Modes


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'points')
    list_display_links = ('id', 'user')
    # search_fields = ('user',)
    list_filter = ('level', 'genres', 'mode')


class LevelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class ModesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Profiles, ProfilesAdmin)
admin.site.register(Levels, LevelsAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Modes, ModesAdmin)
