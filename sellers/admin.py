from django.contrib import admin
from .models import Seller

# Register your models here.
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mvp', 'join_date', 'phone')
    list_display_links = ('id', 'name', 'phone')
admin.site.register(Seller, SellerAdmin)