# Generated by Django 4.1.2 on 2022-10-22 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0004_alter_tournament_is_complete"),
    ]

    operations = [
        migrations.AddField(
            model_name="tournament",
            name="max_players",
            field=models.IntegerField(default=16),
            preserve_default=False,
        ),
    ]
