from django.db import models

# Create your models here.
class StoreBase(models.Model):
    team_name=models.CharField(max_length=200)
    stadium_name=models.CharField(max_length=200, null=True, blank=True)
    # completed= models.BooleanField(default=False)