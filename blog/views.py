from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Blog
from .forms import CommentForm
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView


class HomeBlog(ListView):
    model=Blog
    template_name='blog/index_blog.html'
    context_object_name='blog'
    paginate_by = 1

def index_blog(request):
    blog = Blog.objects.all()
    #objects = ['techno', 'house', 'deep', 'nudisco', 'techstep', 'bigbeat']
    paginator = Paginator(blog, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    context = {'content': blog,
               'title': 'Список статей',
               'page_obj': page_objects}
    return render(request, 'blog/index_blog.html', context)

def view_blog(request,blog_id):
    blog_item=Blog.objects.get(pk=blog_id)
    return render(request, 'blog/single.html',{"blog_item":blog_item})

def add_comment_article(request):
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['name'],
                             form.cleaned_data['content'], 'evgen.guk@ukr.net', ['evgen.guk@yandex.ru'],
                             fail_silently=False)
            return redirect('blog')
    else:
        form=CommentForm()
    return render(request,'blog/add_comment.html',{'form':form})

# def views_blog(request,blog_id):
#     blog_item=Blog.objects.get(pk=blog_id)
#     return render(request, 'blog/single.html',{'blog_item':blog_item})

# class ViewBlog(DetailView):
#     model=Blog
#     blog = Blog.objects.all()
#     template_name = 'blog/single.html'
#     pk_url_kwarg ='blog_id'
#     context_object_name='blog'