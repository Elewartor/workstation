from django.db import models

# Create your models here.

class Unit(models.Model):
    title               = models.CharField(max_length=50, null=False, blank=False)
    upc                 = models.CharField(max_length=12, null=False, blank=False)
    part_number         = models.CharField(max_length=10, null=False, blank=False)
    image_url           = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.title