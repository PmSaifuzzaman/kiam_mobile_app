# collectionpostapp/serializers.py

from rest_framework import serializers
from .models import CollectionPost

class CollectionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionPost
        fields = '__all__'
