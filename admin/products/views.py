from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product, User
from rest_framework import viewsets, status
from rest_framework.views import APIVIEW
from rest_framework.response import Response
import random
from .producer import publish

# Create your views here.


class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        serializer = ProductSerializer(products, many=True)
        publish()
        return Response(serializer.data)


    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_CREATED)

    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class userApiView(APIVIEW):

    def get(self, request):
        user = User.objects.all()
        user = random.choices(user)
        return Response({
            'id': user.id
            })
