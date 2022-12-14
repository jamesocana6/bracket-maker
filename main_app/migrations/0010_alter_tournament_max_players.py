# Generated by Django 4.1.2 on 2022-10-24 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0009_remove_tournament_host_tournament_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tournament",
            name="max_players",
            field=models.IntegerField(
                choices=[(2, "2"), (4, "4"), (8, "8"), (16, "16"), (32, "32")],
                default=8,
            ),
        ),
    ]
