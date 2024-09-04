
#myproject/urls.py

from django import views
from django.contrib import admin
from django.urls import path, include
from app1 import views as app1_views  
from app2 import views as app2_views
from productapp import views as product_views
from bankinfoapp import views as bankinfo_views
from employeeapp import views as employee_views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('app2/', include('app2.urls')),
    path('tbinfo/', app1_views.table_datainfo),
    # URL for retrieving data
    path('tbinfo/<int:pk>/', app1_views.table_datains),

    # Update data using PUT request
    path('tbinfo/update/<int:pk>/', app1_views.UpdateTableData.as_view(), name='update-table-data'),

    #delete data 
    path('tbinfo/delete/<int:pk>/', app1_views.DeleteTableDataView.as_view(), name='delete-table-data'),
    # post data
    path('tbinfo/create/', app1_views.CreateDataView.as_view(), name='create-data'),
    # message table view
    path('app2/message', app2_views.CreateMessageView.as_view(), name='create-data'),
    # Include the authentication app's URL patterns here
    path('authentication/', include('authentication.urls')),
    # product table view
    path('app2/product', product_views.CreateProductView.as_view(), name='create-data'),

    #product info
    path('productinfo/', product_views.product_datainfo),  
    
    #bankinfo 
    path('bankinfo/', bankinfo_views.bankinfo_views),
    path('bankapp/bank', bankinfo_views.CreateBankView.as_view(), name='create-data'),
  

    #employee info
    path('employeeinfo/', employee_views.employee_datainfo),
    path('employeeapp/employee', employee_views.CreateEmployeeView.as_view(), name='create-data'),

    #order post
    path('api/', include('orderapp.urls')),
    
    #visit post
    path('api/', include('visitapp.urls')),

    #leave post
    path('api/', include('leaveapp.urls')),

    #payslip post
    path('payslip/', include('payslipapp.urls')),

    #notification post
    path('notify/', include('notificationapp.urls')),

    #collection post
    path('', include('collectionpostapp.urls')),
    #collection get
    path('api/', include('collectionpostapp.urls')),

       
]















