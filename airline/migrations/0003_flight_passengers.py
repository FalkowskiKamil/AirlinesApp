# Generated by Django 4.1.7 on 2023-04-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("airline", "0002_alter_passager_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="flight",
            name="passengers",
            field=models.ManyToManyField(
                blank=True, related_name="flight_passager", to="airline.passager"
            ),
        ),
    ]
