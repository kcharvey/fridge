from django.db import models

class Food(models.Model):

    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=30)
