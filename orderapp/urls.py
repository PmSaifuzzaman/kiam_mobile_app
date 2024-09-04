# orderapp/urls.py

from django.urls import path
from .views import OrderCreateView
from .views import OrderListView

from . import views

urlpatterns = [
   
    path('api/orderpostinfo/', views.OrderCreateView.as_view(), name='order-create'),

    path('api/orderpostinfo/list/', OrderListView.as_view(), name='order-list'),
]
