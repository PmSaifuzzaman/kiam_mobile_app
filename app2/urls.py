# urls.py in your Django app
from django.urls import path
from .views import CreateMessageView

urlpatterns = [
    path('api/messages/', CreateMessageView.as_view(), name='create_message'),
]
