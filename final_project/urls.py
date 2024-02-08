"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from finalapp.views import usignup, ulogin, uforgotpassword, home, ulogout, contact, feedback, about, settings, services

urlpatterns = [
    path('admin/', admin.site.urls),   
    path("", usignup, name='usignup'),
    path("ulogin/", ulogin, name='ulogin'),
    path('about/', about, name='about'),
    path("settings/", settings, name='settings'),
    path('uforgotpassword/', uforgotpassword, name='uforgotpassword'),
    path("home/", home, name='home'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),    
    path('feedback/', feedback, name='feedback'),
    path("ulogout/", ulogout, name='ulogout'),   
]
