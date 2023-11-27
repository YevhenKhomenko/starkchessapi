# Generated by Django 4.2.6 on 2023-11-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_score',
            new_name='score',
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic_num',
            field=models.IntegerField(default=0, verbose_name='User profile picture number'),
        ),
    ]