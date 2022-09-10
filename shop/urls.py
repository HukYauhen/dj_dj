from django.urls import path
from .views import *

urlpatterns=[
    path('', index_shop, name='shop'),
    path('shop/mail',mail, name='mail'),
]