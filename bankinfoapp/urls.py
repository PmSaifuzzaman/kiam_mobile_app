# urls.py in your Django app

from django.urls import path
from .views import CreateBankView

urlpatterns = [
    path('api/bank/', CreateBankView.as_view(), name='create_bankinfo'),
]
