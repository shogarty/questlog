# Generated by Django 4.2.9 on 2024-09-08 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_campaign_dm_alter_campaign_players'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campaign',
            options={'permissions': (('dm_auth', 'DM Authority'), ('player_auth', 'Player Authority'))},
        ),
        migrations.AlterModelOptions(
            name='quest',
            options={'permissions': (('dm_auth', 'DM Authority'),)},
        ),
    ]