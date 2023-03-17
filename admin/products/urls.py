from django.contrib import admin
from django.urls import path
from .views import ProductViewSet, userApiView

urlpatterns = [
    path('products/', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),

    path('products/<str:pk>/', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'post': 'destroy',
    })),
    path('users/', userApiView.as_view()),
]