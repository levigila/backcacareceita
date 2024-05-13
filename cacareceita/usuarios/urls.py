from django.urls import path
from.import views


urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('loginerror/', views.login_error, name='loginerror'),
    path('esqueciSenha/', views.esqueciSenha, name='esqueci-senha'),
    path('alterarSenha/<int:cod>/', views.alterarSenha, name='alterar-senha'),
    path('verificaoSenha/', views.verificacao, name='verificacao-senha'),
    path('plataforma/', views.plataforma, name='PlataForma'),
    path('receitaAprendiz/', views.receitaAprendiz, name='receitaAprendiz'),
    path('receitaSubChef/', views.receitaSubChef, name='receitaSubChef'),
    path('receitaMiniChef/', views.receitaMiniChef, name='receitaMiniChef'),
    path('receitaConfeiteiro/', views.receitaConfeiteiro, name='receitaConfeiteiro'),
    path('receitaChef/', views.receitaChef, name='receitaChef'),
    path('receitaVegano/', views.receitaVegano, name='receitaVegano'),
    path('buscaReceitaAprendiz/', views.buscaReceitaAprendiz, name='buscaReceitaAprendiz'),
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
    path('homeVegano/', views.homeVegano, name='homeVegano'),
    path('livroReceitaAprendiz/', views.livroReceitaAprendiz, name='livroReceitaAprendiz'),
    path('minhasReceitasAprendiz/', views.minhasReceitasAprendiz, name='minhasReceitasAprendiz'),
    path('logout/', views.logout_view, name='logout'),

        # Assinatura
    path('assinaturaAprendiz/', views.assinaturaAprendiz, name='assinatura-aprendiz'),
    path('assinaturaAprendizInfo1/', views.assinaturaAprendizInfor1, name='assinatura-aprendiz-info1'),
    path('assinaturaAprendizInfo2/', views.assinaturaAprendizInfor2, name='assinatura-aprendiz-info2'),

    # Perfil -> Alterar Senha
    path('alterarSenha/', views.alterarSenha, name='alterar-senha'),
    path('novaSenha/', views.novaSenha, name='nova-senha'),
]