from django.urls import re_path
from CriptoApp import views

urlpatterns = [
    re_path(r'^cadastra_usuario/$', views.CadastrarUsuario.as_view(), name='cadastrarUsuario'),
    re_path(r'^criar_carteira/$', views.CriarCarteira.as_view(), name='criarCarteira'),
    re_path(r'^consulta_usuario/$', views.ConsultaUsuario.as_view(), name='consultaUsario'),
    re_path(r'^consulta_carteira/$', views.ConsultaCarteira.as_view(), name='consultaCarteira'),
    re_path(r'^registra_ativo/$', views.registrarAtivos.as_view(), name='registrarCarteira'),
]