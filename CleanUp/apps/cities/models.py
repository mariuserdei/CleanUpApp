from django.db import models

# Create your models here.
class Cities(models.Model):
    name = models.CharField(max_length=50,  help_text="enter city name")
    zip_code = models.PositiveIntegerField(help_text="enter your city's zip code")

    def __str__(self):
        return self.name