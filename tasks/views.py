import random

from django.http import HttpResponseRedirect

from .forms import LevelA
from googletrans import Translator
from yandex_music import Client
import pytz
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from loginsys.models import Profiles
from songs.models import Songs
import datetime


def tasks(request):
    # инициализация
    user = User.objects.get(id=request.user.id)
    person = Profiles.objects.get(user=request.user.id)

    # получение предпочтительных жанров
    all_genres = []
    for i in person.genres.all():
        all_genres.append(i.id)

    # генерация песен
    ids = []
    for genre in all_genres:
        if genre == 1:
            for i in range(0, 6):
                id_ = random.randint(1, 61)
                ids.append(id_)
        elif genre == 2:
            for i in range(0, 6):
                id_ = random.randint(62, 113)
                ids.append(id_)
        elif genre == 3:
            for i in range(0, 6):
                id_ = random.randint(114, 161)
                ids.append(id_)
        elif genre == 4:
            for i in range(0, 6):
                id_ = random.randint(162, 203)
                ids.append(id_)
        elif genre == 5:
            for i in range(0, 6):
                id_ = random.randint(204, 248)
                ids.append(id_)
        elif genre == 6:
            for i in range(0, 6):
                id_ = random.randint(249, 253)
                ids.append(id_)
        elif genre == 7:
            for i in range(0, 6):
                id_ = random.randint(254, 291)
                ids.append(id_)
        elif genre == 8:
            for i in range(0, 6):
                id_ = random.randint(292, 319)
                ids.append(id_)
        elif genre == 9:
            for i in range(0, 6):
                id_ = random.randint(320, 340)
                ids.append(id_)
        elif genre == 10:
            for i in range(0, 6):
                id_ = random.randint(341, 393)
                ids.append(id_)
        elif genre == 11:
            for i in range(0, 6):
                id_ = random.randint(394, 402)
                ids.append(id_)

    while len(ids) != 6:
        index = random.randint(0, len(ids) - 1)
        ids.remove(ids[index])

    # получение нужных песен
    songs = []
    for i in ids:
        songs.append(Songs.objects.get(id=i))

    context = {'title': 'Задания',
               'songs': songs}
    return render(request, 'tasks/tasks_page.html', context)


def task_theory(request, id_):
    # инициализация
    user = User.objects.get(id=request.user.id)
    person = Profiles.objects.get(user=request.user.id)

    # получение песни
    song = Songs.objects.get(id=id_)

    # получение id трека, исполнителя и альбома
    client = Client().init()

    string = client.search(song.title + ' ' + song.artist).best.result

    track_id = string.id
    artist_id = string.artists[0].id
    album_id = string.albums[0].id

    # уровни A
    if str(person.level) == 'A1' or str(person.level) == 'A2':
        level = True
        translator = Translator()
        translation = translator.translate(song.lyrics, src='en', dest='ru')
        translation = translation.text
    else:
        level = False
        translation = 'Отсутствует'

    context = {'title': f'Песня {song.title} :: Шаг 1',
               'song': song,
               'track_id': track_id,
               'artist_id': artist_id,
               'album_id': album_id,
               'translation': translation,
               'level': level}
    return render(request, 'tasks/tasks_theory_page.html', context)


context_ = {}
result_1 = []


def task_exercises(request, id_):
    global context_
    global result_1
    # инициализация
    user = User.objects.get(id=request.user.id)
    person = Profiles.objects.get(user=request.user.id)

    # получение песни
    song = Songs.objects.get(id=id_)

    # получение id трека, исполнителя и альбома
    client = Client().init()

    string = client.search(song.title + ' ' + song.artist).best.result

    track_id = string.id
    artist_id = string.artists[0].id
    album_id = string.albums[0].id

    # деление песни на строки и запись их в массив
    strings = song.lyrics.split('\n')
    for i in strings:
        if i == '':
            strings.remove(i)

    # деление песни на слова и запись их в массив
    words = song.lyrics.split(' ')
    index = 0
    for i in words:
        i = i.replace('\n', ' ')
        words[index] = i

        i = i.replace('(', '')
        words[index] = i

        i = i.replace(')', '')
        words[index] = i

        index += 1

    # первое задание
    def creating_task_1(count):
        # определение первой строки
        if len(strings) >= count * 2:
            els = round((len(strings) / 2) - count)
        else:
            els = 0

        # создание копии строк
        strings_a1 = strings

        # генерация
        result = []
        index = random.randint(0, els) * 2
        for i in range(0, count):
            result.append(strings[index])
            strings_a1.remove(strings[index])

        # удаление слова из строк
        task_1_d = {}
        number = 1
        for i in result:
            str_now = i.split(' ')
            index = random.randint(0, len(str_now))
            word = str_now[index - 1]
            str_now[index - 1] = f'__({number})__'
            number += 1
            task_1_d[' '.join(str_now)] = word
            result_1.append(' '.join(str_now))

        return task_1_d

    # второе задание
    def creating_task_2(count):
        task_2_d = {}
        for i in range(0, count):
            # генерация слова
            word = ''
            while len(word) < 4:
                word = words[random.randint(0, len(words))]
                word = word.split(' ')[0]

            word = word.replace(',', '')
            word = word.replace('.', '')
            word = word.replace('!', '')
            word = word.replace('?', '')
            word = word.replace(':', '')
            word = word.replace('"', '')
            word = word.lower()

            # перевод слова
            translator = Translator()
            translation_1 = translator.translate(str(word), src='en', dest='ru')
            translation_1 = translation_1.text

            # генерация неправильных слов
            wrong_context = {}
            task_2_wrong = []
            for j in range(0, 3):
                one = ''

                one = words[random.randint(0, len(words))]
                one = one.split(' ')[0]

                one = one.replace(',', '')
                one = one.replace('.', '')
                one = one.replace('!', '')
                one = one.replace('?', '')
                one = one.replace(':', '')
                one = one.replace('"', '')
                one = one.replace("'", '')

                translator = Translator()
                translation = translator.translate(str(one), src='en', dest='ru')
                translation = translation.text
                task_2_wrong.append(translation.lower())

            wrong_context[translation_1] = task_2_wrong
            task_2_d[word] = wrong_context
        return task_2_d

    # размещение текста песни
    level = True

    # context
    context_['title'] = f'Песня {song.title} :: Шаг 2'
    context_['song'] = song
    context_['track_id'] = track_id
    context_['artist_id'] = artist_id
    context_['album_id'] = album_id
    context_['level'] = level

    # создание заданий в зависимости от уровня
    if str(person.level) == 'A1' or str(person.level) == 'A2':
        context_['task_1_d'] = creating_task_1(8)
        context_['count_1'] = [1, 2, 3, 4, 5, 6, 7, 8]

        context_['task_2_d'] = creating_task_2(4)
        context_['count_2'] = [1, 2, 3, 4]
    elif str(person.level) == 'B1' or str(person.level) == 'B2':
        context_['task_1_d'] = creating_task_1(12)
        context_['count_1'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        context_['task_2_d'] = creating_task_2(6)
        context_['count_2'] = [1, 2, 3, 4, 5, 6]
    elif str(person.level) == 'C1' or str(person.level) == 'C2':
        context_['task_1_d'] = creating_task_1(16)
        context_['count_1'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16]

        context_['task_2_d'] = creating_task_2(8)
        context_['count_2'] = [1, 2, 3, 4, 5, 6, 7, 8]

    if request.method == 'POST':
        form = LevelA(request.POST)
        if form.is_valid():
            task_1 = form.cleaned_data
            # redirect('task_check')
    else:
        form = LevelA()
    context_['form'] = form

    return render(request, 'tasks/tasks_exercises_page.html', context_)


# def task_check(request):
#     context = {'title': 'Проверка'}
#     # проверка первого задания
#     index = 0
#     print(result_1)
#     for i in result_1:
#         print(i)
#         print(context_['task_1_d'])
#         index += 1
#
#     return render(request, 'tasks/task_check_page.html', context)


def task_check(request, id_):
    song = Songs.objects.get(id=id_)

    context = {'title': f'Песня {song.title} :: Проверка',
               'song': song}
    return render(request, 'tasks/task_check_page.html', context)
