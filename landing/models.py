from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="personal_url")
    content = models.TextField(blank=True)
    picture = models.ImageField()

    def get_absolute_url(self):
        return reverse('product_link', kwargs={'slud_id': self.slug})

