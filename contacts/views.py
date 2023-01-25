from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        product = request.POST['product']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        username = request.POST['username']
        address = request.POST['address']

        contact = Contact(product= product, product_id=product_id, name=name, email=email, phone=phone,
        user_id=user_id, username=username, address=address,)
        contact.save()

        messages.success(request, 'Your request has been submitted, our office will confirm you soon.')
        return redirect('/products/'+product_id)