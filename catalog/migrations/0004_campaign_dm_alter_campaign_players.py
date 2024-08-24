# Generated by Django 4.2.9 on 2024-08-24 22:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0003_alter_character_campaign_alter_character_player_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='dm',
            field=models.ManyToManyField(related_name='rev_dm', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='players',
            field=models.ManyToManyField(related_name='rev_players', to=settings.AUTH_USER_MODEL),
        ),
    ]