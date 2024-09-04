# visitapp/admin.py

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Visit

@admin.register(Visit)
class VisitAdmin(ImportExportModelAdmin):
    list_display = ('id','date', 'pf_no', 'dealer_code', 'route', 'outlet', 'start_time', 'end_time', 'visit_type', 'description')
    search_fields = ['id', 'date', 'pf_no', 'dealer_code', 'route', 'outlet', 'visit_type', 'description']

    