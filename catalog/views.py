from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Campaign, Quest, Character
import guardian
from guardian.shortcuts import assign_perm




UserModel = get_user_model()

# Create your views here.

def index(request):
    """View function for home page of site."""

    # The 'all()' is implied by default.

    num_campaigns = Campaign.objects.all().count()
    num_quests = Quest.objects.all().count()

    context = {
        'num_campaigns': num_campaigns,
        'num_quests' : num_quests

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)




class CampaignListView(generic.ListView):
    model = Campaign
    context_object_name = 'campaign_list'

class CharacterListView(generic.ListView):
    model = Character
    context_object_name = 'character_list'

class QuestListView(generic.ListView):
    model = Quest
    context_object_name = 'quest_list'

class CampaignDetailView(generic.DetailView):
    model = Campaign

class CharacterDetailView(generic.DetailView):
    model = Character

class QuestDetailView(generic.DetailView):
    model = Quest

class CampaignCreate(LoginRequiredMixin, CreateView):
    Model = Campaign
    fields = ['name']
    
    def form_valid(self, form):
        form.instance.dm = self.request.user
        form.instance.players = self.request.user
        assign_perm('dm_auth', self.request.user, self.object)
        assign_perm('player_auth', self.request.user, self.object)
        return super().form_valid(form)
    
class CampaignUpdate(PermissionRequiredMixin, UpdateView):
    model = Campaign
    permission_required = ['dm_auth']
    fields = ['name', 'players','dm']

    def form_valid(self, form):
        for p in self.instance.players:
            assign_perm('player_auth', p, self.object)

        for d in self.instance.dm:
            assign_perm('dm_auth', d, self.object)
        return super().form_valid(form)



class UserCurrentCampaignsView(LoginRequiredMixin, generic.ListView):
    """Generic class based view listing a user's current campaigns"""

    model = Campaign
    template_name = "catalog/user_current_campaigns.html"
    paginate_by =  10

    def get_queryset(self):
        return(
            Campaign.objects.filter(players=self.request.user)
        )


    
