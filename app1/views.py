from django.shortcuts import render
from .models import TableData
from . serializers import TableDataSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


# Create your views here.
# Queryset

def table_datainfo(request):
    # complex data
    tb = TableData.objects.all()
    # python dict
    serializer = TableDataSerializer(tb, many=True)
    # render Json
    json_data = JSONRenderer().render(serializer.data)
    # json sent to user
    return HttpResponse(json_data, content_type='application/json')

# model instance

def table_datains(request, pk):
    # complex data
    tb = TableData.objects.get(id=pk)
    # python dict
    serializer = TableDataSerializer(tb)
    # render Json
    json_data = JSONRenderer().render(serializer.data)
    # json sent to user
    return HttpResponse(json_data, content_type='application/json')




class UpdateTableData(APIView):
    def put(self, request, pk):
        try:
            table_data = TableData.objects.get(pk=pk)
        except TableData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TableDataSerializer(table_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#delete data class
class DeleteTableDataView(generics.DestroyAPIView):
    queryset = TableData.objects.all()
    serializer_class = TableDataSerializer 
    

#post data

class CreateDataView(generics.CreateAPIView):
    queryset = TableData.objects.all()
    serializer_class = TableDataSerializer          
