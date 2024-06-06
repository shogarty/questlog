from django.shortcuts import render
from .models import Game, Character, Quest

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
