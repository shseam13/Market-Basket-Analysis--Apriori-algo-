from django.shortcuts import render
from django.http import HttpResponse
from products.choices import catagory_choices,price_choices

from products.models import Product
from sellers.models import Seller
# Create your views here.
def index(request):
    products = Product.objects.order_by('id').filter(is_published=True)[:3]
    context = {
        'products': products,
        'catagory_choices': catagory_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    sellers = Seller.objects.order_by('id')
    # Get MVP
    mvp_sellers = Seller.objects.all().filter(is_mvp=True)

    context = {
        'sellers': sellers,
        'mvp_sellers': mvp_sellers
    }
    return render(request, 'pages/about.html', context)