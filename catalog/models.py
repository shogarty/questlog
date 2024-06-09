from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.contrib.auth import get_user_model
from django.conf import settings
import uuid

UserModel = get_user_model()


#potential idea: two separate classes, Character and DM, inherit from player.
#this makes it so a player can be a character in one campaign and a DM in another
#as well as allowing for different characters in each campaign
#does DM need it's own class?

class Game(models.Model):
    "Represents a specific game instance"
    #Unique Name
    #unique game id?
    #Can have any number of players, and any number of DM's.
    #Should DM's count as a kind of player?
    #Can have any number of quests. Quest attributes should be handled in their own model
    name = models.CharField(max_length=512, null=False)
    dm = models.ManyToManyField(UserModel)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular game instance."""
        return reverse('game-detail', args=[str(self.id)])


class Character(models.Model):
    name = models.CharField(max_length=512, null=False)
    player = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False, blank=False)
    game = models.ForeignKey(Game, null=False, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular character instance."""
        return reverse('character-detail', args=[str(self.id)])


class Quest(models.Model):
    name = models.CharField(max_length=512, null=False)
    game = models.ForeignKey(Game, null=False, on_delete=models.CASCADE)
    #give quest a visibility attribute. If null, visible by all. 
    #else, visible only by the characters explicitly listed, and the DM.
    visible = models.ManyToManyField(Character)
    summary = models.TextField(
        max_length=10000)
    is_complete = models.BooleanField(default=False)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular character instance."""
        return reverse('character-detail', args=[str(self.id)])






