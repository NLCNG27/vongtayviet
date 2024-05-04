"""vongtayviet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# Path: vongtayviet/urls.py
from django.contrib import admin
from django.urls import path
from jobs import views as jobs_views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs_views.home_view, name='home'),
    path('home/', jobs_views.home_view, name='home'),
    path('job_listing/', jobs_views.job_listing_view, name='job_listing'),
    path('contact.html', jobs_views.contact_view, name='contact'),
    path('register/', accounts_views.register_view, name='register'),
    path('login/', accounts_views.login_view, name='login'),

]
