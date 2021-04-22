from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cadastro$', views.cadastro, name='cadastro'),
    url(r'^login$', views.login_cliente, name='login'),
    url(r'^logout$', views.logout_cliente, name='logout'),
    url(r'^login_adm$', views.login_adm, name='login_adm'),
]