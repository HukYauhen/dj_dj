from django.db import models

class Shop(models.Model):
    title = models.CharField(max_length=150,verbose_name='Название товара')
    content = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name='Фото')
    price=models.DecimalField(max_digits=15, decimal_places=2,verbose_name='Цена товара')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Товар'
        verbose_name_plural = 'Товары'
        ordering=['price']
