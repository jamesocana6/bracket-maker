# Generated by Django 4.1.2 on 2022-10-22 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0003_alter_tournament_is_complete"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tournament",
            name="is_complete",
            field=models.BooleanField(default=False),
        ),
    ]
