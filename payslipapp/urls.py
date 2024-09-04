# urls.py
from django.urls import path
from .views import PayslipListView
from .views import PayslipListView, save_pdf

urlpatterns = [
    path('paysliplist/', PayslipListView.as_view(), name='payslip-list'),
    path('save-pdf/<int:payslip_id>/', save_pdf, name='save-pdf'),  # Include payslip_id
]
