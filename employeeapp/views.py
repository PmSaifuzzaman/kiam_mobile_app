#views.py

from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CreateEmployeeView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



# Queryset

def employee_datainfo(request):
    # complex data
    tb = Employee.objects.all()
    # python dict
    serializer = EmployeeSerializer(tb, many=True)
    # render Json
    json_data = JSONRenderer().render(serializer.data)
    # json sent to user
    return HttpResponse(json_data, content_type='application/json')