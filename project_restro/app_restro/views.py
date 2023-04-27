from django.shortcuts import render, redirect
from .forms import CategoryCreateForm, MenuCreateForm
from .models import Category, MenuModel

# Create your views here.

#Views for menu page
def menu_index(request):
    data=MenuModel.objects.all()
    context={"data":data}
    return render(request, 'menus/index.html',context)

def menu_add(request):
    menu_form = MenuCreateForm()
    context={
        "form":menu_form,
        "title":"Menu Creatiom Form"
    }
    if request.method=="POST":
        id = request.POST.get('category_id')
        category_id=Category.objects.get(id=id)
        data=MenuModel()
        data.menu_title=request.POST.get('menu_title')
        data.menu_desc=request.POST.get('menu_desc')
        data.menu_ingredient=request.POST.get('menu_ingredient')
        data.menu_price=request.POST.get('menu_price')
        data.category_id=category_id
        data.save()

        #pass and save data using argumented constructor
        # menu_title=request.POST.get('menu_title')
        # menu_desc=request.POST.get('menu_desc')
        # menu_ingredient=request.POST.get('menu_ingredient')
        # menu_price=request.POST.get('menu_price')
        # data=MenuModel(menu_title=menu_title, menu_desc=menu_desc, menu_ingredient=menu_ingredient, menu_price=menu_price)
        # data.save()

        #pass and save directly from form object
        # data=MenuCreateForm(request.POST)
        # if data.is_valid():
        #     data.save()
    return render(request, 'menus/create.html', context)

def menu_edit(request, id):
    data=MenuModel.objects.get(id=id)
    context={"data":data}
    return render(request, 'menus/edit.html', context)

def menu_update(request):
    if request.method=="POST":
        data=MenuCreateForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect("menu-list")
    return redirect("menu-list")

def menu_detail(request, id):
    data=MenuModel.objects.get(id=id)
    context={"data":data}
    return render(request, 'menus/show.html', context)

def menu_delete(request, id):
    data=MenuModel.objects.get(id=id)
    data.delete()
    return (redirect, 'menu-list')

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