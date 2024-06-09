from django.contrib import admin
from Profiles.models import User

# Register your models here.
from .models import Game, Character, Quest

admin.site.register(Game)
admin.site.register(Character)
admin.site.register(Quest)
admin.site.register(User)