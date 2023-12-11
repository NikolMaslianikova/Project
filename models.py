from django.contrib.auth.models import User
from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    count = models.IntegerField()


class PurchaseRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)


class Demand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicines = models.ManyToManyField(Medicine, blank=True)
