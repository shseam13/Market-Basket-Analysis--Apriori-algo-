from django.db import models
from datetime import datetime
from sellers.models import Seller

# Create your models here.
class Product(models.Model):
    '''Extends the models class.'''
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    product_id = models.IntegerField()
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    min_order = models.IntegerField()
    price = models.IntegerField()
    catagory = models.CharField(max_length=200)
    delevary = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    def __str__(self) -> str:
        return self.title
