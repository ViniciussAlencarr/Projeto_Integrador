from django.urls import path, include
from .views import *

urlpatterns = [
    path('cadastro', cadastro, name="cadastro"),
    path('login', login_cliente, name='login'),
    path('logout', logout_cliente, name='logout'),
    path('login_adm', login_adm, name='login_adm'),
]