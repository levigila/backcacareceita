from django.urls import path
from.import views


urlpatterns = [
    path ('cadastro/', views.cadastro, name='cadastro'),
    path ('login/', views.login, name='login'),
    path ('plataforma/', views.plataforma, name='PlataForma'),
    path('loginerror/', views.login_error, name='loginerror')  ,  
    path('receita/', views.receita, name='receita'),
    path('loginerror/', views.login_error, name='loginerror'),
    path('buscaReceitaAprendiz/', views.buscaReceitaAprendiz, name='buscaReceitaAprendiz')
]