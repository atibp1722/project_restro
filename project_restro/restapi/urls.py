from django.urls import path
from .views import CategoryApiView, MenuApiView

urlpatterns=[
    path('category/',CategoryApiView.as_view()),
    path('menu/',MenuApiView.as_view())
]