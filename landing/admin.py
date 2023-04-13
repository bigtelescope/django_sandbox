from django.contrib import admin

from landing.models import Product

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Product, ProductAdmin)
