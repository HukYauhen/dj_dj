from django.contrib import admin
from .models import Shop

class ShopAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','price','photo')
    list_display_links=('price','title')
    search_fields=('id','title')

admin.site.register(Shop,ShopAdmin)