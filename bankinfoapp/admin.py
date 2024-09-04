#admin.py

#resources section
from import_export import resources
from .models import Bank
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

class BankResource(resources.ModelResource):
    class Meta:
        model = Bank
        fields = ('id','bank_code','bank_name','account_no','branch')

@admin.register(Bank)
class BankAdmin(ImportExportModelAdmin):
    list_display = ['id','bank_code','bank_name','account_no','branch']
    resource_class = BankResource
