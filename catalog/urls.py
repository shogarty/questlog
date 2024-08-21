from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mycampaigns/', views.UserCurrentCampaignsView.as_view(), name = 'my-campaigns')
]
