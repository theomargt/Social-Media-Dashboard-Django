"""
URL configuration for social_media_dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#from dashboard.views import dashboard_view  # ✅ Import the dashboard view

#urlpatterns = [
    #path("admin/", admin.site.urls),  
    #path("", dashboard_view, name="home"),  # ✅ Set dashboard as homepage
    #path("dashboard/", include("dashboard.urls")),  # ✅ Include dashboard URLs
#]

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # ✅ Import redirect function

# ✅ Function to redirect root URL ("/") to the dashboard
def redirect_to_dashboard(request):
    return redirect('dashboard')  # Redirect "/" to "/dashboard/"

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ Django Admin Panel
    path('dashboard/', include('dashboard.urls')),  # ✅ Include dashboard app URLs
    path('', redirect_to_dashboard, name='home'),  # ✅ Redirect root URL to dashboard
]