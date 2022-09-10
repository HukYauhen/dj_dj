from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','created_at','photo')
    list_display_links=('id','title')
    search_fields=('id','title')

admin.site.register(News,NewsAdmin)