from django.db import models


# Create your models here.
class PricingPlan(models.Model):
    name = models.CharField('Name of plan', max_length=50, unique=True)
    amount = models.DecimalField('Price for plan', max_digits=4, decimal_places=2, default=0)
