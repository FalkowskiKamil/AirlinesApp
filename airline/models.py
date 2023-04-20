from django.db import models
from django.conf import settings
# Create your models here.
class Airport(models.Model):
    airport_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    departures = models.ManyToManyField('Flight', related_name='departure_airports', blank=True)
    arrivals = models.ManyToManyField('Flight', related_name='arrival_airports', blank=True)

    def __str__(self):
        return f"{self.name}"

class Flight(models.Model):
    start = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_flights')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_flights')
    date = models.DateTimeField()
    def clean(self):
        if self.start == self.destination:
            raise ValueError("Start and destination cannot be the same.")
        
    def __str__(self):
        return f'{self.id}'
    
    def formatted_date(self):
        return self.date.strftime('%d-%m-%Y')
        
class PassagerFake(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    flights = models.ManyToManyField(Flight, related_name='passengers', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.surname}"
    
class Route(models.Model):
    start = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_routes')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_routes')
    flights = models.ManyToManyField(Flight, related_name='routes')
    
    def __str__(self):
        return f"{self.id}"
    
class Passager(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="passager_user"
    )
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    flights = models.ManyToManyField(Flight, related_name='passager', blank=True)
    def __str__(self):
        return f"{self.first_name, self.surname}"