# Generated by Django 4.1.7 on 2023-03-18 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0008_remove_passager_flights'),
    ]

    operations = [
        migrations.AddField(
            model_name='passager',
            name='flights',
            field=models.ManyToManyField(related_name='lol', to='airline.flight'),
        ),
    ]
