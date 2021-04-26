"""BankingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from BankingSystem.views import hello_Ever
from BankingSystem.views import index_page,home_view,home_view1

from BankingSystem.views import AboutUs

from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',hello_Ever),
    path('',index_page),
    path('home/',home_view),
    path('home1/',home_view1),
    path('about/',AboutUs.as_view()),
    path('customer/',include("CustomerApp.urls"))
]
