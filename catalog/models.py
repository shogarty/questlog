from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.contrib.auth.models import User
import uuid


#potential idea: two separate classes, Character and DM, inherit from player.
#this makes it so a player can be a character in one campaign and a DM in another
#as well as allowing for different characters in each campaign
#does DM need it's own class?

class Game(models.Model):
    "Represents a specific campaign instance"
    #Unique Name
    #unique game id?
    #Can have any number of players, and any number of DM's.
    #Should DM's count as a kind of player?
    #Can have any number of quests. Quest attributes should be handled in their own model
    name = models.CharField(max_length=512, null=False)
    dm = models.ManyToManyField('Player', null=False)

class Player(models.Model):
    #Unique username
    #maybe unique userid? Use uuid?
    #Can be part of any number of games.
    #Can be both dm and regular player in different games
    name = models.CharField(max_length=512, null=False)

    

class Character(models.Model):
    name = models.CharField(max_length=512, null=False)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, null=False, on_delete=models.CASCADE)


class Quest(models.Model):
    game = models.ForeignKey(Game, null=False, on_delete=models.CASCADE)
    #give quest a visibility attribute. If null, visible by all. 
    #else, visible only by the characters explicitly listed, and the DM.
    visible = models.ManyToManyField(Character, null=True)
    summary = models.TextField(
        max_length=10000)
    is_complete = models.BooleanField(default=False)





