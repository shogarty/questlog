from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.contrib.auth import get_user_model
from django.conf import settings
import uuid

UserModel = get_user_model()

# Create your models here.

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    subdomain_prefix = models.CharField(max_length=100, unique=True)
    players = models.ManyToManyField(UserModel)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a particular Tenant instance."""
        return reverse('tenant-detail', args=[str(self.id)])

class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Quest(TenantAwareModel):
    name = models.CharField(max_length=512, null=False)
    #give quest a visibility attribute. If null, visible by all. 
    #else, visible only by the characters explicitly listed, and the DM.
    summary = models.TextField(
        max_length=10000)
    is_complete = models.BooleanField(default=False)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular quest instance."""
        return reverse('quest-detail', args=[str(self.id)])
    
class Character(TenantAwareModel):
    name = models.CharField(max_length=512, null=False)
    player = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular character instance."""
        return reverse('character-detail', args=[str(self.id)])
