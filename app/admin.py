from django.contrib import admin
from .models import Product, ProductTracker

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'trackers__tracking_id']

class ProductTrackerAdmin(admin.ModelAdmin):
    search_fields = ['tracking_id', 'name__name']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductTracker, ProductTrackerAdmin)