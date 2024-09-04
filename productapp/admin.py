
#admin.py

#resources section
from import_export import resources
from .models import Product
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id','sku','name','price','uom','line')

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['id','sku','name','price','uom','line']
    resource_class = ProductResource




