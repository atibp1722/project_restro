from django.urls import path
from . import views

urlpatterns=[
    path('menu/',views.menu_index, name='menu-list'),
    path('menu/add',views.menu_add, name='menu-list'),
    path('menu/edit',views.menu_edit, name='menu-list'),
    path('menu/show',views.menu_detail, name='menu-list'),

    path('order/',views.order_index, name='order-list'),
    path('order/add',views.order_add, name='order-list'),
    path('order/edit',views.order_edit, name='order-list'),
    path('order/show',views.order_detail, name='order-list'),

    path('customer/',views.customer_index, name='customer-list'),
    path('customer/add',views.customer_add, name='customer-list'),
    path('customer/edit',views.customer_edit, name='customer-list'),
    path('customer/show',views.customer_detail, name='customer-list'),

    path('authenticate/',views.authenticate_index, name='authenticate-list'),
    path('authenticate/login',views.authenticate_login, name='authenticate-list'),
    path('authenticate/register',views.authenticate_register, name='authenticate-list')

]