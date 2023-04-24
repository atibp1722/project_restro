from django.shortcuts import render

# Create your views here.

#Views for menu page
def menu_index(request):
    return render(request, 'menus/index.html')
def menu_add(request):
    return render(request, 'menus/create.html')
def menu_edit(request):
    return render(request, 'menus/edit.html')
def menu_detail(request):
    return render(request, 'menus/show.html')

# Views for order page
def order_index(request):
    return render(request, 'orders/index.html')
def order_add(request):
    return render(request, 'orders/create.html')
def order_edit(request):
    return render(request, 'orders/edit.html')
def order_detail(request):
    return render(request, 'orders/show.html')

# Views for customer page
def customer_index(request):
    return render(request, 'customers/index.html')
def customer_add(request):
    return render(request, 'customers/create.html')
def customer_edit(request):
    return render(request, 'customers/edit.html')
def customer_detail(request):
    return render(request, 'customers/show.html')

# Views for authentication
def authenticate_index(request):
    return render(request, 'authentication/login.html')
def authenticate_login(request):
    return render(request, 'authentication/login.html')
def authenticate_register(request):
    return render(request, 'authentication/register.html')