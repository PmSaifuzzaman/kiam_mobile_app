#admin.py

#resources section
from import_export import resources
from .models import Employee
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
        fields = ('id','pf_no','employee_name','territory','party_name','party_code','line')

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    list_display = ['id','pf_no','employee_name','territory','party_name','party_code','line']
    resource_class = EmployeeResource
