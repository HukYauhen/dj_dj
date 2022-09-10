from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index_news(request):
    news = News.objects.all()
    context = {'content': news,
               'title': 'Список новостей'}
    return render(request, 'news/index_news.html', context)