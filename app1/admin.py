# from django.contrib import admin
# from . models import TableData


# # Register your models here.
# @admin.register(TableData)
# class TableDataAdmin(admin.ModelAdmin):
#     list_display=['id','name','department','pf_no']



#admin.py

#resources section
from import_export import resources
from .models import TableData
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

class TableDataResource(resources.ModelResource):
    class Meta:
        model = TableData
        fields = ('id','name','department','pf_no')

@admin.register(TableData)
class TableDataAdmin(ImportExportModelAdmin):
    list_display = ['id','name','department','pf_no']
    resource_class = TableDataResource

