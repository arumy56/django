from django.db import models

# Create your models here.
class Match(models.Model):
    home_team=models.CharField(max_length=200)
    away_team=models.CharField(max_length=200)
    # home_score=models.IntegerField()
    # away_score=models.IntegerField()
    match_date=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.home_team
        


