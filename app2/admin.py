
#admin.py

#resources section
from import_export import resources
from .models import Message
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

class MessageResource(resources.ModelResource):
    class Meta:
        model = Message
        fields = ('id', 'text1', 'text2')

@admin.register(Message)
class MessageAdmin(ImportExportModelAdmin):
    list_display = ['id', 'text1', 'text2']
    resource_class = MessageResource




