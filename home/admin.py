from django.contrib import admin
from .models import Home

class HomeAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','photo')
    list_display_links=('id','title')
    search_fields=('id','title')

admin.site.register(Home,HomeAdmin)
