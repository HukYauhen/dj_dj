from django.urls import path
from .views import *

urlpatterns= [
    path('', HomeMood.as_view(), name='mood'),
    path('category/<int:category_id>/', MoodByCategory.as_view(), name='category'),
    path('mood/add_comment',add_comment, name='add_comment'),
]