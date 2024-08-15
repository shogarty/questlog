from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.contrib.auth import get_user_model
from django.conf import settings
from Tenants.models import Tenant, TenantAwareModel
import uuid

UserModel = get_user_model()


#potential idea: two separate classes, Character and DM, inherit from player.
#this makes it so a player can be a character in one campaign and a DM in another
#as well as allowing for different characters in each campaign
#does DM need it's own class?




class Character(TenantAwareModel):
    name = models.CharField(max_length=512, null=False)
    player = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular character instance."""
        return reverse('character-detail', args=[str(self.id)])


 




