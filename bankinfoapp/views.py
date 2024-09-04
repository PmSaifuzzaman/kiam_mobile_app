#views.py

from rest_framework import generics
from .models import Bank
from .serializers import BankSerializer
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CreateBankView(generics.CreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


# Create your views here.
# Queryset

def bankinfo_views(request):
    # complex data
    tb = Bank.objects.all()
    # python dict
    serializer = BankSerializer(tb, many=True)
    # render Json
    json_data = JSONRenderer().render(serializer.data)
    # json sent to user
    return HttpResponse(json_data, content_type='application/json')