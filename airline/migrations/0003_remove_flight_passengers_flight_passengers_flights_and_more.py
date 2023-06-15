# Generated by Django 4.1.7 on 2023-06-15 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("airline", "0002_alter_flightpassager_flight_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="flight",
            name="passengers",
        ),
        migrations.AddField(
            model_name="flight",
            name="passengers_flights",
            field=models.ManyToManyField(
                blank=True,
                related_name="flights_passengers",
                through="airline.FlightPassager",
                to="airline.passager",
            ),
        ),
        migrations.AlterField(
            model_name="flightpassager",
            name="flight",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="flight_passagers",
                to="airline.flight",
            ),
        ),
        migrations.AlterField(
            model_name="flightpassager",
            name="passager",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="flight_passagers",
                to="airline.passager",
            ),
        ),
        migrations.AlterField(
            model_name="passager",
            name="flights",
            field=models.ManyToManyField(
                related_name="passagers",
                through="airline.FlightPassager",
                to="airline.flight",
            ),
        ),
        migrations.AddConstraint(
            model_name="flightpassager",
            constraint=models.UniqueConstraint(
                fields=("flight", "passager"), name="unique_flight_passager"
            ),
        ),
    ]
