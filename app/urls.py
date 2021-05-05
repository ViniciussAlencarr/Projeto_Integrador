from django.urls import path, include
from .views import *

urlpatterns = [
    path('cadastro', cadastro, name="cadastro"),
    path('login', login_cliente, name='login'),
    path('login_adm', login_adm, name='login_adm'),
    path('logout/<int:pk>/', logout_cliente, name='logout'),
    path('logout_adm/<int:pk>/', logout_adm, name='logout_adm'),
]