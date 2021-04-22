"""project URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
from app.views import home, splashScreen, cadastro, form, form_User, create, createUser, delete, view, update, edit, login_cliente, logout_cliente, login_adm

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('app.urls')),
    path('', splashScreen, name='splashScreen'),
    path('accounts/', include('allauth.urls')),
    path('home/', home, name='home'),
    path('form/', form, name='form'),
    path('form_User/', form_User, name='form_User'),
    path('create/', create, name='create'),
    path('login_cliente/', login_cliente, name='login_cliente'),
    path('login_adm/', login_adm, name='login_adm'),
    path('logout_cliente/', logout_cliente, name='logout_cliente'),
    path('createUser/', createUser, name='createUser'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('view/<int:pk>/', view, name='view'),
    path('update/<int:pk>/', update, name='update'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('view/<int:pk>/', view, name='view'),
   
]
