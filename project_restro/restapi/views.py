from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.request import Request
from app_restro.models import Category, MenuModel
from .serializers import CategorySerializer, MenuSerializer

# Create your views here.

class CategoryApiIdView(APIView):
    #Object create so edit, show, edelete can be done from one place using id
    def get_object(self, id):
        try:
            data=Category.objects.get(id=id)
            return data
        except Category.DoesNotExist:
            return None
        
    #call the object
    def get(self, request, id):
        data=self.get_object(id)
        if not data:
            return Response({"message":"No data found"}, status=status.HTTP_404_NOT_FOUND)
        serializer=CategorySerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryApiView(APIView):
    def get(self, request):
        categories=Category.objects.all()
        if not Category.DoesNotExist:
            return Response({"mesaage": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer=CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data=request.data
        # data= request.POST from form data
        serializer=CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuApiView(APIView):
    def get(self, request):
        menus=MenuModel.objects.all()
        if not MenuModel.DoesNotExist:
            return Response({"mesaage": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer=MenuSerializer(menus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data=request.data
        serializer=MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)