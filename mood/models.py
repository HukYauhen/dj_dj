from django.db import models
from django.urls import reverse


class Mood(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    # style = models.CharField(max_length=50,verbose_name='Стилистика')
    content = models.TextField(verbose_name='Создание настроения')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    size = models.TimeField(verbose_name='Длительность')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Превью')
    audio = models.FileField(upload_to='audios/%Y/%m/%d/', verbose_name='Компиляция')
    category = models.ForeignKey('Category', on_delete=models.PROTECT,
                                 verbose_name='Стилистика')

    def funct(self):
        return 'Приятного прослушивания'

    def get_absolute_url(self):
        return reverse('views_mood',kwargs={'mood_id':self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настроение'
        verbose_name_plural = 'Настроения'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True,
                             verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category',kwargs={'category_id':self.pk})



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
