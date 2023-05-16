"""website URL Configuration

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
from django.urls import path,include
from signup.views import signaction
from login.views import loginaction,home
from mobile.views import mob
from contact.views import contactINF
from django.views.generic import TemplateView


urlpatterns = [
   # path('login/',include("login.urls"))
    path('',include('login.urls')),
    path('login/',loginaction),
    path('admin/', admin.site.urls),
    path('signup/',signaction),
    path('mobile/',mob),
    path('contact/',contactINF),
    path('login/welcome.html', TemplateView.as_view(template_name='welcome.html')),


]
