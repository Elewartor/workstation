from django.db import models
from account.models import Account

# Create your models here.


class Category(models.Model):
    title               = models.CharField(max_length=30, null=False, blank=False, unique=True)

    def __str__(self):
        return self.title

class Unit(models.Model):
    title               = models.CharField(max_length=50, null=False, blank=False)
    upc                 = models.CharField(max_length=12, null=False, blank=False)
    part_number         = models.CharField(max_length=10, null=False, blank=False)
    image_url           = models.CharField(max_length=500, null=False, blank=False)
    details             = models.TextField(max_length=9000, null=True, blank=True)
    author              = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    category            = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title