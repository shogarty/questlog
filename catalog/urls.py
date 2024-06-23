from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('mygames/', views.CurrentUserGamesView.as_view(), name='my-games')
]
