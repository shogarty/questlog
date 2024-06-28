from django.shortcuts import render
from .models import Game, Character, Quest
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

UserModel = get_user_model()

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_games = Game.objects.all().count()
    num_characters = Character.objects.all().count()
    num_quests = Quest.objects.all().count()

    # The 'all()' is implied by default.

    context = {
        'num_games': num_games,
        'num_characters':num_characters,
        'num_quests':num_quests,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class CurrentUserGamesView(LoginRequiredMixin, generic.ListView):
    model = Game
    template_name = 'catalog/user_game_list.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            Game.objects.filter(players=self.request.user) | Game.objects.filter(dm=self.request.user)
        )
