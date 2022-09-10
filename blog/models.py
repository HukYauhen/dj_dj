from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=150,verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateField(auto_now_add=True,verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name='Превью')

    def get_absolute_url(self):
        return reverse('view_blog', kwargs={"blog_id":self.pk})

    def __str__(self):
        return self.content

    class Meta:
        verbose_name='Cтатья'
        verbose_name_plural = 'Статьи'
        ordering=['created_at']
