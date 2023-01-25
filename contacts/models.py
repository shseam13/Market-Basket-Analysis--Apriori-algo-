from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    product = models.CharField(max_length=200)
    product_id = models.IntegerField()
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    purchase_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self) -> str:
        return self.name