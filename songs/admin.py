from django.contrib import admin
from .models import Songs


class SongsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'difficulty', 'limit')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'artist', 'genre')
    list_filter = ('genre', 'limit')


admin.site.register(Songs, SongsAdmin)
