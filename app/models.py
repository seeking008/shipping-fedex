import uuid
from django.db import models
from django.contrib.auth.models import User

class Support(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} from {self.name}"


class ShippingInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shipping to {self.full_name} - {self.city}, {self.country}"

class Product(models.Model):
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField()


    def __str__(self):
        return self.name


class ProductTracker(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='trackers', null=True, blank=True)
    tracking_id = models.CharField(max_length=100, unique=True, editable=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.tracking_id:
            self.tracking_id = self.generate_tracking_id()
        super().save(*args, **kwargs)

    def generate_tracking_id(self):
        prefix = "FDX"
        while True:
            tracking_id = f"{prefix}-{uuid.uuid4().hex[:10].upper()}"
            if not ProductTracker.objects.filter(tracking_id=tracking_id).exists():
                return tracking_id

    def __str__(self):
        return f"Tracking ID for {self.name.name}: {self.tracking_id}"
