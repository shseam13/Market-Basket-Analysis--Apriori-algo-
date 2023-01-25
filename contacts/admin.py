from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id',  'name', 'product', 'email', 'purchase_date')
    list_display_links = ('id', 'name', 'product')
    search_fields = ('name', 'email', 'product')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)