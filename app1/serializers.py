from rest_framework import serializers
from .models import TableData

class TableDataSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=25)
    department=serializers.CharField(max_length=25)
    pf_no=serializers.IntegerField()

#for updating data 

class TableDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableData
        fields = '__all__'

    def update(self, instance, validated_data):
        # Update the instance with the validated data
        instance.name = validated_data.get('name', instance.name)
        instance.department = validated_data.get('department', instance.department)
        instance.pf_no = validated_data.get('pf_no', instance.pf_no)
        instance.save()
        return instance
   