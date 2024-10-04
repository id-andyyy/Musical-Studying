from django.db import models
from django.contrib.auth.models import User


class Profiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, verbose_name='пользователь')
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото')
    age = models.IntegerField(verbose_name='возраст')
    level = models.ForeignKey('Levels', on_delete=models.PROTECT, verbose_name='уровень английского')
    genres = models.ManyToManyField('Genres', verbose_name='жанры')
    mode = models.ForeignKey('Modes', on_delete=models.PROTECT, verbose_name='режим тренировки')
    is_adult_content = models.BooleanField(default=True, verbose_name='просмотр контента для несовершеннолетних')
    is_signup = models.BooleanField(default=False, verbose_name='подписка на новости')
    perfect = models.TextField(blank=True, verbose_name='упражнения идеальные')
    mistakes = models.TextField(blank=True, verbose_name='упражнения с ошибками')
    points = models.IntegerField(default=0, verbose_name='опыт')
    was_online = models.DateTimeField(auto_now_add=True, verbose_name='последняя активность')
    last_songs = models.TextField(blank=True, verbose_name='последние песни')
    data_joined = models.DateTimeField(auto_now_add=True, verbose_name='дата регистрации')

    # def __str__(self):
    #     return self.id

    class Meta:
        db_table = 'all_users'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['-data_joined', 'id']


class Levels(models.Model):
    title = models.CharField(max_length=2, verbose_name='название уровня английского')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'levels'
        verbose_name = 'уровень английского'
        verbose_name_plural = 'уровни английского'
        ordering = ['id']


class Genres(models.Model):
    title = models.CharField(max_length=50, verbose_name='название жанра')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'genres'
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'
        ordering = ['id']


class Modes(models.Model):
    title = models.CharField(max_length=50, verbose_name='название режима')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'modes'
        verbose_name = 'режим тренировки'
        verbose_name_plural = 'режимы тренировки'
        ordering = ['id']
