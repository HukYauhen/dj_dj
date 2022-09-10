from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150,verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateField(auto_now_add=True,verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name='Превью',blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Новость'
        verbose_name_plural = 'Новости'
        ordering=['created_at']
