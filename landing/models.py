from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    picture = models.ImageField()
