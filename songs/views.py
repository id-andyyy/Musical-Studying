from django.shortcuts import render
from loginsys.models import Levels, Genres, Modes


def songs(request):
    context = {'title': 'Песни'}
    genres = Genres.objects.all()
    context.update({'genres': genres})
    modes = Modes.objects.all()
    context.update({'modes': modes})

    return render(request, 'songs/songs_page.html', context)
