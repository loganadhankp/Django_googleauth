from django.contrib import admin 
from django.urls import path, include 
from accounts.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include allauth URLs
    path('', home, name='home'),
]
