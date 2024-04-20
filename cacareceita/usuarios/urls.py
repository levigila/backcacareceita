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
    path('loginerror/', views.login_error, name='loginerror'),
    path('buscaReceitaAprendiz/', views.buscaReceitaAprendiz, name='buscaReceitaAprendiz'),
    path('buscaReceitaMiniChef/', views.buscaReceitaMiniChef, name='buscaReceitaMiniChef'),
    path('buscaReceitaSubChef/', views.buscaReceitaSubChef, name='buscaReceitaSubChef'),
    path('buscaReceitaChef/', views.buscaReceitaChef, name='buscaReceitaChef'),
    path('buscaReceitaConfeiteiro/', views.buscaReceitaConfeiteiro, name='buscaReceitaConfeiteiro'),
    path('buscaReceitaVegano/', views.buscaReceitaVegano, name='buscaReceitaVegano'),
    path('homeAprendiz/', views.homeAprendiz, name='homeAprendiz'),
    path('homeMiniChef/', views.homeMiniChef, name='homeMiniChef'),
    path('homeSubChef/', views.homeSubChef, name='homeSubChef'),
    path('homeChef/', views.homeChef, name='homeChef'),
    path('homeConfeiteiro/', views.homeConfeiteiro, name='homeConfeiteiro'),
    path('homeVegano/', views.homeVegano, name='homeVegano')
]