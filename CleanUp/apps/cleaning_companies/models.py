from django.db import models
from CleanUp.apps.cities.models import Cities

# Create your models here.
class CleaningCompany(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField()
    city = models.ManyToManyField(Cities)

    def __str__(self):
        return self.name


    
