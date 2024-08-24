from django.contrib import admin
from .models import Quest, Character, Campaign

# Register your models here.

admin.site.register(Character)
admin.site.register(Quest)
admin.site.register(Campaign)
