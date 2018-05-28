from django.db import models


class StoreItem(models.Model):
    # item_number = models.
    name = models.CharField(max_length=100)
    info_text = models.CharField(max_length=200)
    # price = models.
    # image = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Store(models.Model):
    pass


class Cart(models.Model):
    pass
