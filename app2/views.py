# views.py in your Django app

from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer

class CreateMessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


