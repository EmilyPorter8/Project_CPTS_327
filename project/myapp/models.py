from django.db import models

# Create your models here.

class InventoryItem(models.Model):
    title = models.CharField(max_length = 200)
    amount = models.PositiveBigIntegerField()
    # ID = models.PositiveBigIntegerField()
    date = models.DateField()