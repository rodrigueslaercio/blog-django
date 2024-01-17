"""URL patterns for accounts"""

from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # Default auth urls
    path('', include('django.contrib.auth.urls')),
    # Register page
    path('register', views.register, name='register'),
]