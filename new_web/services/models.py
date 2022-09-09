from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    cost = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Basket(models.Model):
    id = models.IntegerField(primary_key=True)
    cost = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
