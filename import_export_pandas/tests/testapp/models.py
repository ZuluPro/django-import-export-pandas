from django.db import models
from django_pandas.managers import DataFrameManager


class Instance(models.Model):
    name = models.CharField(max_length=50)


class Entry(models.Model):
    timestamp = models.DateTimeField()
    amount = models.IntegerField()
    rate = models.FloatField()
    tag = models.CharField(max_length=100)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)

    objects = DataFrameManager()

    @property
    def amount_x_2(self):
        return self.amount * 2
