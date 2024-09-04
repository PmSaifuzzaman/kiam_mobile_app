
###################################### update###########################

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
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('id', 'date', 'pf_no', 'employee_name', 'party_name', 'party_code', 'total_order_price', 'description', 'download_pdf_button')
    inlines = [OrderItemInline]
    readonly_fields = ('download_pdf_button',)

    def download_pdf_button(self, obj):
        return format_html(f'<a class="button" href="{obj.id}/download_pdf/">Download PDF</a>')

    download_pdf_button.short_description = 'Download PDF'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:order_id>/download_pdf/', self.download_pdf),
        ]
        return custom_urls + urls

    def download_pdf(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id)
        order_items = OrderItem.objects.filter(order=order)

        # Create a PDF response
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="order_{order_id}.pdf"'

        # Create the PDF object, using the response object as its "file."
        doc = SimpleDocTemplate(response, pagesize=A4)
        elements = []

        # Draw order details in a table
        styles = getSampleStyleSheet()
        order_details_data = [
            ["Invoice", "", "", ""],  # Center the "invoice" text
            ["Order ID:", f"{order.id}", "", ""],
            ["Party Name:", f"{order.party_name}", "Date:", f"{order.date}"],
            ["Party Code:", f"{order.party_code}", "Supervisor Name:", f"{order.employee_name}"],
            ["Total Order Value:", f"{order.total_order_price}", "", ""],
            ["Description:", f"{order.description}", "", ""],
        ]

        order_details_table = Table(order_details_data, colWidths=[1.5*inch, 2*inch, 1.5*inch, 2*inch])
        order_details_table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 0), (3, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (3, 0), colors.whitesmoke),
            ('SPAN', (0, 0), (3, 0)),  # Span first row
            ('ALIGN', (0, 0), (3, 0), 'CENTER'),  # Center "invoice" text
            ('SPAN', (1, 1), (3, 1)),  # Span Order ID row
            ('SPAN', (1, 4), (3, 4)),  # Span the description row
            ('SPAN', (1, 5), (3, 5)),  # Span the total order value row
            ('ALIGN', (0, 1), (0, -1), 'RIGHT'),  # Align keys in the first column to the right
            ('ALIGN', (1, 1), (1, -1), 'LEFT'),   # Align values in the second column to the left
            ('ALIGN', (2, 1), (2, -1), 'RIGHT'),  # Align keys in the third column to the right
            ('ALIGN', (3, 1), (3, -1), 'LEFT'),   # Align values in the fourth column to the left
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica')
        ]))

        elements.append(order_details_table)
        elements.append(Spacer(1, 24))  # Add space before the items table

        # Add order items in tabular format
        data = [
            ["SL", "Code", "Product Name", "Qty", "Unit Price", "Total Price"]
        ]

        for i, item in enumerate(order_items, start=1):
            product_code = item.sku
            description = Paragraph(item.product_name, styles['Normal'])
            quantity = item.quantity
            unit_price = item.price
            total_price = quantity * unit_price
            data.append([i, product_code, description, quantity, f"{unit_price:.2f}", f"{total_price:.2f}"])

        table = Table(data, colWidths=[0.5*inch, 1*inch, 3*inch, 1*inch, 1*inch, 1.5*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(table)

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

@admin.register(OrderItem)
class OrderItemAdmin(ImportExportModelAdmin):
    list_display = ('id', 'product_name', 'sku', 'price', 'quantity', 'order')


