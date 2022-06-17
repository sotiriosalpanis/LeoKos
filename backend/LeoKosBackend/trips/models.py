from django.db import models

class Trip(models.Model):

    trip_name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.trip_name}'
