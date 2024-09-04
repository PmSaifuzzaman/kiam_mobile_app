# admin.py
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Leave

@admin.register(Leave)
class LeaveAdmin(ImportExportModelAdmin):
    list_display = ('id','pfNo', 'name', 'startDate', 'endDate', 'days', 'leaveType', 'description')
    search_fields = ('id','pfNo', 'name', 'leaveType')
