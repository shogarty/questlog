from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Campaign, Quest, Character


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

class UserCurrentCampaignsView(LoginRequiredMixin, generic.ListView):
    """Generic class based view listing a user's current campaigns"""

    model = Campaign
    template_name = "catalog/user_current_campaigns.html"
    paginate_by =  10

    def get_queryset(self):
        return(
            Campaign.objects.filter(players=self.request.user)
        )


    
