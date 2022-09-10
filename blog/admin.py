from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','created_at','photo')
    list_display_links=('id','title')
    search_fields=('id','title')

admin.site.register(Blog,BlogAdmin)
