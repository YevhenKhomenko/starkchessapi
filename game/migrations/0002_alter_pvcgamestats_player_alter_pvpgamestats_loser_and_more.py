# Generated by Django 4.2.6 on 2023-10-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvcgamestats',
            name='player',
            field=models.ManyToManyField(to='user_profile.user', verbose_name='Player'),
        ),
        migrations.AlterField(
            model_name='pvpgamestats',
            name='loser',
            field=models.ManyToManyField(blank=True, null=True, related_name='loser', to='user_profile.user', verbose_name='Game loser'),
        ),
        migrations.AlterField(
            model_name='pvpgamestats',
            name='player1',
            field=models.ManyToManyField(related_name='player1', to='user_profile.user', verbose_name='Player 1'),
        ),
        migrations.AlterField(
            model_name='pvpgamestats',
            name='player2',
            field=models.ManyToManyField(related_name='player2', to='user_profile.user', verbose_name='Player 2'),
        ),
        migrations.AlterField(
            model_name='pvpgamestats',
            name='winner',
            field=models.ManyToManyField(blank=True, null=True, related_name='winner', to='user_profile.user', verbose_name='Game winner'),
        ),
    ]
