from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'product_id', 'is_published', 'price', 'list_date', 'seller')
    list_display_links = ('id', 'title', 'seller')
    list_filter = ('seller',)
    search_fields = ('product_id', 'title', 'catagory', 'price')
# Register your models here.
admin.site.register(Product, ProductAdmin)