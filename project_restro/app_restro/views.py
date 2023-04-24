from django.shortcuts import render
from .forms import CategoryCreateForm, MenuCreateForm

# Create your views here.

#Views for menu page
def menu_index(request):
    return render(request, 'menus/index.html')

def menu_add(request):
    menu_form = MenuCreateForm()
    context={
        "form":menu_form,
        "title":"Menu || Create"
    }
    return render(request, 'menus/create.html', context)

def menu_edit(request):
    return render(request, 'menus/edit.html')
def menu_detail(request):
    return render(request, 'menus/show.html')

#Create Category
def category_create(request):
    form=CategoryCreateForm()
    context={
        "form":form,
        "title":"Category || Create"
    }
    return render(request, "menus/add-category.html", context)

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