from django.db import models

# Create your models here.
class Encounter(models.Model):
    encounter_name = models.CharField(max_length=200)


class Creature(models.Model):
    encounter = models.ForeignKey(Encounter, on_delete=models.CASCADE)
    monster_name = models.CharField(max_length=200)
    initiative_value = models.IntegerField()