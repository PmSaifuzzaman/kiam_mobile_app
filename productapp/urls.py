# urls.py in your Django app
from django.urls import path
from .views import CreateProductView

urlpatterns = [
    path('api/product/', CreateProductView.as_view(), name='create_product'),
]