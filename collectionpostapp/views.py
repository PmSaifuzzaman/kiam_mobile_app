# collectionpostapp/views.py
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CollectionPost
from .serializers import CollectionPostSerializer

@api_view(['POST'])
def collection_post_info(request):
    if request.method == 'POST':
        serializer = CollectionPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CollectionPostList(generics.ListAPIView):
    queryset = CollectionPost.objects.all()
    serializer_class = CollectionPostSerializer