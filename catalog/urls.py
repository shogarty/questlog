from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mycampaigns/', views.UserCurrentCampaignsView.as_view(), name = 'my-campaigns'),
    path('campaign/<int:pk>', views.CampaignDetailView.as_view(), name='campaign-detail'),
    path('character/<int:pk>', views.CharacterDetailView.as_view(), name='character-detail'),
    path('quest/<int:pk>', views.QuestDetailView.as_view(), name='quest-detail'),
    path('campaign/create/', views.CampaignCreate.as_view(), name='campaign-create'),
    path('campaign/<int:pk>/edit/', views.CampaignUpdate.as_view(), name='campaign-update')
]
