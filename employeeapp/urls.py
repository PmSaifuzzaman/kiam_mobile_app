# urls.py in your Django app

from django.urls import path
from .views import CreateEmployeeView

urlpatterns = [
    path('api/employee/', CreateEmployeeView.as_view(), name='create_employee'),
]