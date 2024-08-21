from django.shortcuts import render

from .models import Quest, Character
from django.contrib.auth import get_user_model

from .utilities import get_tenant

UserModel = get_user_model()

# Create your views here.


def campaign(request):
    tenant = get_tenant(request)
    quests = Quest.objects.filter(tenant=tenant)
    characters = Character.objects.filter(tenant=tenant)

    return render(request, 'tenant/campaign.html', {'tenant': tenant, 'quests': quests, 'characters': characters})