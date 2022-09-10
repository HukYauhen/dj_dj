from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Home

def index_home(request):
    home = Home.objects.all()
    context = {'content': home,
               'title': 'Главная'}
    return render(request, 'home/index_home.html', context)


class Search(ListView):
    template_name='home/search.html'
    context_object_name = 'content'
    paginate_by = 1

    def get_queryset(self):
     return Home.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['s']=f"s={self.request.GET.get('s')}&"
        return context