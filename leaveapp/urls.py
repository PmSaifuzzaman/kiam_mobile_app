# urls.py
from django.urls import path
from .views import LeaveListView

urlpatterns = [
    path('api/leavelist/', LeaveListView.as_view(), name='leave-list'),
]
