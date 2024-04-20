from django.urls import path
from.import views


urlpatterns = [
    path ('cadastro/', views.cadastro, name='cadastro'),
    path ('login/', views.login, name='login'),
    path ('plataforma/', views.plataforma, name='PlataForma'),


    path('loginerror/', views.login_error, name='loginerror')  ,  
    path('receitaAprendiz/', views.receitaAprendiz, name='receitaAprendiz')  ,  
    path('receitaSubChefe/', views.receitaSubChefe, name='receitaSubChefe')  ,  
    path('receitaMiniChefe/', views.receitaMiniChefe, name='receitaMiniChefe')  ,  
    path('receitaConfeiteiro/', views.receitaConfeiteiro, name='receitaConfeiteiro')  ,  
    path('receitaChefe/', views.receitaChefe, name='receitaChefe')  ,  
    path('receitaVegano/', views.receitaVegano, name='receitaVegano')  ,  
    path('loginerror/', views.login_error, name='loginerror'),
    path('buscaReceitaAprendiz/', views.buscaReceitaAprendiz, name='buscaReceitaAprendiz'),
    path('loginerror/', views.login_error, name='loginerror')  ,  
    path('receita/', views.receita, name='receita'),
    path('loginerror/', views.login_error, name='loginerror'),
    path('buscaReceitaAprendiz/', views.buscaReceitaAprendiz, name='buscaReceitaAprendiz')
]