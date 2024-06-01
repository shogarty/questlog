from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.contrib.auth.models import User


class Game(Model):
    name = CharField(max_length=512, null=False)

class Player(Model):
    is_dm = BooleanField(default=False)
    game = ForeignKey(to=Game, on_delete=CASCADE, related_name="players")
    user = ForeignKey(to=settings.AUTH_USER_MODEL, related_name="playing")

class Quest(Model):
    game = ForeignKey(to=Game, on_delete=CASCADE, related_name="quests")
    is_complete = BooleanField(default=False)
    details = ...




