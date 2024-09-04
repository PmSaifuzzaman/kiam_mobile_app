#admin.py

#resources section
# from import_export import resources
# from .models import CollectionPost
# from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin

# class CollectionResource(resources.ModelResource):
#     class Meta:
#         model = CollectionPost
#         fields = ('id','date','pf_no','employee_name','party_name','party_code','account_no','amount','description')

# @admin.register(CollectionPost)
# class CollectionAdmin(ImportExportModelAdmin):
#     list_display = ['id','date','pf_no','employee_name','party_name','party_code','account_no','amount','description']
#     resource_class = CollectionResource


#############################################
from import_export import resources
from django.contrib import admin
from django.urls import path
from django.utils.html import format_html
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageTemplate, Frame
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from import_export.admin import ImportExportModelAdmin
from .models import CollectionPost

class CollectionResource(resources.ModelResource):
    class Meta:
        model = CollectionPost
        fields = ('id', 'date', 'pf_no', 'employee_name', 'party_name', 'party_code', 'account_no', 'amount', 'description')

@admin.register(CollectionPost)
class CollectionAdmin(ImportExportModelAdmin):
    list_display = ['id', 'date', 'pf_no', 'employee_name', 'party_name', 'party_code', 'account_no', 'amount', 'description', 'download_pdf_button']
    resource_class = CollectionResource
    readonly_fields = ('download_pdf_button',)

    def download_pdf_button(self, obj):
        return format_html(f'<a class="button" href="{obj.id}/download_pdf/">Download PDF</a>')

    download_pdf_button.short_description = 'Download PDF'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:collection_id>/download_pdf/', self.download_pdf),
        ]
        return custom_urls + urls

    def download_pdf(self, request, collection_id, *args, **kwargs):
        collection = get_object_or_404(CollectionPost, pk=collection_id)

        # Create a PDF response
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="collection_{collection_id}.pdf"'

        # Create the PDF object, using the response object as its "file."
        doc = SimpleDocTemplate(response, pagesize=A4)
        elements = []

        # Draw collection details in a table
        styles = getSampleStyleSheet()
        collection_details_data = [
            ["Collection", "", "", ""],  # Center the "invoice" text
            ["Collection ID:", f"{collection.id}", "", ""],
            ["Party Name:", f"{collection.party_name}", "Date:", f"{collection.date}"],
            ["Party Code:", f"{collection.party_code}", "Supervisor Name:", f"{collection.employee_name}"],
            ["Total Amount:", f"{collection.amount}", "", ""],
            ["Description:", f"{collection.description}", "", ""],
        ]

        collection_details_table = Table(collection_details_data, colWidths=[1.5*inch, 2*inch, 1.5*inch, 2*inch])
        collection_details_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 0), (3, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (3, 0), colors.whitesmoke),
            ('SPAN', (0, 0), (3, 0)),  # Span first row
            ('ALIGN', (0, 0), (3, 0), 'CENTER'),  # Center "invoice" text
            ('SPAN', (1, 1), (3, 1)),  # Span Collection ID row
            ('SPAN', (1, 5), (3, 5)),  # Span the description row
            ('ALIGN', (0, 1), (0, -1), 'RIGHT'),  # Align keys in the first column to the right
            ('ALIGN', (1, 1), (1, -1), 'LEFT'),   # Align values in the second column to the left
            ('ALIGN', (2, 1), (2, -1), 'RIGHT'),  # Align keys in the third column to the right
            ('ALIGN', (3, 1), (3, -1), 'LEFT'),   # Align values in the fourth column to the left
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica')
        ]))

        elements.append(collection_details_table)
        elements.append(Spacer(1, 24))  # Add space before the items table

        # Define a frame to add page numbers
        frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
        template = PageTemplate(id='test', frames=frame, onPage=self.add_page_number)
        doc.addPageTemplates([template])

        # Build the PDF
        doc.build(elements)

        return response

    def add_page_number(self, canvas, doc):
        page_num = canvas.getPageNumber()
        text = f"Page {page_num}"
        canvas.drawRightString(A4[0] - inch, 0.75 * inch, text)
