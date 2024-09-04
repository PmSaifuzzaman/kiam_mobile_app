from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CreateProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Create your views here.
# Queryset

def product_datainfo(request):
    # complex data
    tb = Product.objects.all()
    # python dict
    serializer = ProductSerializer(tb, many=True)
    # render Json
    json_data = JSONRenderer().render(serializer.data)
    # json sent to user
    return HttpResponse(json_data, content_type='application/json')