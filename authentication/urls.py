from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('login/', views.login_view, name='login'),
    path('login/', obtain_auth_token),
    # Example login URL pattern
    # Add other URL patterns for registration, logout, etc., as needed.
]

