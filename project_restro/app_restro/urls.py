from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('menu/',views.menu_index, name='menu-list'),
    path('menu/add',views.menu_add, name='menu-add'),
    path('menu/update',views.menu_update, name='menu-update'),
    path('menu/edit/<int:id>/',views.menu_edit, name='menu-edit'),
    path('menu/show/<int:id>/',views.menu_detail, name='menu-show'),
    path('menu/delete/<int:id>/',views.menu_delete, name='menu-delete'),

    path('category/create/', views.category_create, name='category-add'),

    # """ path('order/',views.order_index, name='order-list'),
    # path('order/add',views.order_add, name='order-add'),
    # path('order/edit',views.order_edit, name='order-edit'),
    # path('order/show',views.order_detail, name='order-show'),

    # path('customer/',views.customer_index, name='customer-list'),
    # path('customer/add',views.customer_add, name='customer-add'),
    # path('customer/edit',views.customer_edit, name='customer-edit'),
    # path('customer/show',views.customer_detail, name='customer-show'),

    # path('authenticate/',views.authenticate_index, name='authenticate-list'),
    # path('authenticate/login',views.authenticate_login, name='authenticate-list'),
    # path('authenticate/register',views.authenticate_register, name='authenticate-list') """

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)