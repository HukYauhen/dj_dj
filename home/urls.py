from django.urls import path
from .views import *

urlpatterns=[
    path('', index_home, name='home'),
    path('search/',Search.as_view(),name='search'),
]