from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .product_relation import product_dictionary

from contacts.models import Contact
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Register User
        # Check if password match
        if password == password2:
            # Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is already taken.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used.')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password, 
                    first_name=first_name, last_name=last_name,)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are logged in.')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are registered and can log in.')
                    return redirect('login')

        else:
            messages.error(request, 'Password do no match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # Log in User
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username/password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Successfully logged out.')
        return redirect('index')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-purchase_date').filter(user_id=request.user.id)
    predictive_product = []
    for contact in user_contacts:
        for k,v in product_dictionary.items():
            if k.lower() == contact.product.lower():
                predictive_product.append(v.title())
            elif v.lower() == contact.product.lower():
                predictive_product.append(k.title())

    context = {
        'pred_products': predictive_product,
    }
    return render(request, 'accounts/dashboard.html', context)