from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Product
from .choices import catagory_choices,price_choices

# Create your views here.
def index(request):
    products = Product.objects.order_by('id').filter(is_published=True)

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {
        'products': page_listings
    }
    return render(request, 'products/products.html', context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'products/product.html', context)

def search(request):
    query_list = Product.objects.order_by('id')
    
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(description__icontains = keywords)
    
    # Catagory
    if 'catagory' in request.GET:
        catagory = request.GET['catagory']
        if catagory:
            query_list = query_list.filter(catagory__iexact = catagory)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_list = query_list.filter(price__lte = price)

    context = {
        'catagory_choices': catagory_choices,
        'price_choices': price_choices,
        'products': query_list,
        'values': request.GET,
    }
    return render(request, 'products/search.html', context)