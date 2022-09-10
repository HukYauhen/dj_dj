from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Mood, Category

class MoodAdminForm(forms.ModelForm):
    content=forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model=Mood
        fields='__all__'

class MoodAdmin(admin.ModelAdmin):
    form=MoodAdminForm
    list_display = ('id','title','content','category','created_at','size','photo','audio')
    list_display_links=('title','content')
    search_fields=('title','style')
    list_filter=('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links=('title','id')
    search_fields=('title',)

admin.site.register(Mood,MoodAdmin)
admin.site.register(Category,CategoryAdmin)
