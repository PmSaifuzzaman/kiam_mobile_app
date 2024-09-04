# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Leave
from .serializers import LeaveSerializer

class LeaveListView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': 'Data posted successfully'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'message': 'Error posting data'}, status=status.HTTP_400_BAD_REQUEST)
