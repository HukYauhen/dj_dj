from django.urls import path
from .views import *

urlpatterns=[
    path('', index_blog, name='blog'),
    path('blog/<int:blog_id>',view_blog,name='view_blog'),
    path('blog/add_comment_article',add_comment_article, name='add_comment_article'),

]