from django.shortcuts import render

from .models import Quest

from .utilities import get_tenant

# Create your views here.


def our_quests(request):
    tenant = get_tenant(request)
    quests = Quest.objects.filter(tenant=tenant)

    return render(request, 'tenant/our_quests.html', {'tenant': tenant, 'quests': quests})