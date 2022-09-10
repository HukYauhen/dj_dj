from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=150,verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name='Превью')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name='Представление'
        verbose_name_plural = 'Представления'
        ordering=['title']
