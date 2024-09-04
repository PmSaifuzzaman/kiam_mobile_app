# admin.py
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Payslip

@admin.register(Payslip)
class PayslipAdmin(ImportExportModelAdmin):
    list_display = ('id', 'pfNo', 'name', 'startDate', 'endDate', 'payslipType', 'pdf_file_display')
    search_fields = ('id', 'pfNo', 'name', 'payslipType')

    def pdf_file_display(self, obj):
        if obj.pdf_file:
            return f'<a href="{obj.pdf_file.url}" target="_blank">Download PDF</a>'
        return "No PDF"

    pdf_file_display.short_description = "PDF File"
    pdf_file_display.allow_tags = True
