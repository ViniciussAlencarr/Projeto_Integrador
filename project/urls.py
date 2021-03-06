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
from app.views import *

urlpatterns = [
path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', splashScreen, name='splashScreen'),
    path('adm/', homeAdm, name='homeAdm'),
    path('clientes/', adm_Cliente, name='clientes_Adm'),
    path('cliente/', homeCliente, name='homeCliente'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('view/<int:pk>/<str:username>/', view, name='view'),
    path('resultado/<int:pk>/', resultadoFinal, name='resultadoFinal'),
    path('update/<int:pk>/', update, name='update'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('view/<int:pk>/', view, name='view'),
    path('solicitacoes/', solicitacoes, name='solicitacoes'),
    path('solicitacoesClientes/', solicitacoesAdm, name='solicitacoesAdm'),
    path('documentos/', docs, name='docs'),
]
