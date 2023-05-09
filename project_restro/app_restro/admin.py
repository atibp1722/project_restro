from django.contrib import admin
from .models import Category, MenuModel

# Register your models here.

class AdminMenu(admin.ModelAdmin):
    list_display = ('menu_title', 'category_id', 'menu_price')
    search_fields=('menu_title', )
    list_filter = ('menu_price', )

class AdminCategory(admin.ModelAdmin):
    list_display = ('category_name', )

admin.site.register(Category, AdminCategory)
admin.site.register(MenuModel, AdminMenu)

admin.site.index_title= "Restaurant Management Suite"
admin.site.site_header="Admin Panel"