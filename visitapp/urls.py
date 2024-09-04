# orderapp/urls.py

from django.urls import path
from .views import CreateVisitView
from visitapp.views import VisitListView
from . import views

urlpatterns = [
    #post visit
    path('api/visitpostinfo/', views.CreateVisitView.as_view(), name='visit-create'),
    #fetch json in flutter
    path('api/visitpostinfo/list/', VisitListView.as_view(), name='visit-list'),
    
]
