from django.shortcuts import render
from .models import Character
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

    # The 'all()' is implied by default.

    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

