from rest_framework import serializers
from app_restro.models import Category, MenuModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields=("category_name", )
        model=Category

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        fields=("menu_title", "category_id", "menu_desc", "menu_price", "menu_ingredient")
        model=MenuModel