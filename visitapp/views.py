# views.py in your Django app

from rest_framework import generics
from .models import Visit
from .serializers import VisitSerializer

class CreateVisitView(generics.CreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class VisitListView(generics.ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
