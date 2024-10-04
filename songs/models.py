from django.db import models
from loginsys.models import Genres


class Songs(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    artist = models.CharField(max_length=150, verbose_name='исполнитель')
    genre = models.ForeignKey(Genres, on_delete=models.PROTECT, null=True, verbose_name='жанр')
    difficulty = models.IntegerField(verbose_name='сложность')
    limit = models.BooleanField(verbose_name='контент, содержащий нецензурную лексику')
    link = models.CharField(blank=True, max_length=150, verbose_name='ссылка')
    lyrics = models.TextField(verbose_name='текст')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'all_songs'
        verbose_name = 'песня'
        verbose_name_plural = 'песни'
        ordering = ['id', 'title']
