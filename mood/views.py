from django.shortcuts import render
from django.http import HttpResponse
from .models import Mood, Category
from django.views.generic import ListView, DetailView


class HomeMood(ListView):
    model=Mood
    template_name='mood/home_mood_list.html'
    context_object_name='mood'
    paginate_by = 1


class MoodByCategory(ListView):
    model=Mood
    template_name = 'mood/home_mood_list.html'
    context_object_name = 'mood'

    def get_queryset(self):
     return Mood.objects.filter(category_id=self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']=Category.objects.get(pk=self.kwargs['category_id'])
        return context


def add_comment(request):
    return render(request,'mood/add_comment.html')

