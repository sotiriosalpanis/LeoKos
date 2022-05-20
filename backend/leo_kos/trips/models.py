from djongo import models

class Trip(models.Model):
    name = models.CharField(max_length=50)


    class Meta:
        abstract = True


# Create your models here.
