# Generated by Django 4.0.2 on 2024-05-27 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_guild_skill_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='bio',
            field=models.CharField(max_length=255),
        ),
    ]