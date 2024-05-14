from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import CustomUser
from .models import CustomUserManager
from django.contrib.auth import authenticate, login as login_django, logout
from django.urls import reverse
from .forms import RegistroForm, LoginForm  # Importando o novo formulário

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirma_senha = request.POST.get('confirma_senha')

        # Check if the user already exists
        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'cadastroerrornome.html')

        # Check if a user with the same email already exists
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'cadastroerroremail.html')

        # # Check if passwords match
        if senha != confirma_senha:
            return render(request, 'cadastroerrorsenha.html')

        # Create the user with hashed password
        else:
            user = CustomUser.objects.create_user(username=username, email=email, password=senha)
            user.save()
             # Authenticate the user and log them in
        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login_django(request, user)
            return redirect('homeAprendiz')  # Redirecionar para a página homeAprendiz
        else:
            # Tratar erro de autenticação, se necessário
            pass


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['senha']
            CustomUser = authenticate(username=username, password=password)

            if CustomUser is not None:
                login_django(request, CustomUser)
                return redirect('homeAprendiz')
            else:
                form.add_error(None, 'Usuário ou senha inválidos.')
                return render(request, 'loginerror.html')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
        logout(request)
        return redirect('homeAprendiz')

def esqueciSenha(request):
    if request.method == "POST":
        return render(request, 'verificacaoSenha.html')
    return render(request, 'esqueciSenha.html')


def verificacao(request):
    if request.method == "POST":
        print(request.POST.get('cod-otp4'))
        return render(request, 'alterarSenha.html')

    return render(request, 'verificacaoSenha.html')


def alterarSenha(request, cod):
    if request.method == "POST":

        cod = request.POST.get('cod-otp1')
        print(cod)
        pass
    return render(request, 'alterarSenha.html')


def receitaAprendiz(request):
    if request.method == "GET":
        return render(request, 'ReceitaAprendiz.html')


def receitaSubChef(request):
    if request.method == "GET":
        return render(request, 'ReceitaSubChef.html')


def plataforma():
    pass


def receitaMiniChef(request):
    if request.method == "GET":
        return render(request, 'ReceitaMiniChef.html')


def receitaConfeiteiro(request):
    if request.method == "GET":
        return render(request, 'ReceitaConfeiteiro.html')


def receitaVegano(request):
    if request.method == "GET":
        return render(request, 'ReceitaVegano.html')


def receitaChef(request):
    if request.method == "GET":
        return render(request, 'ReceitaChef.html')


def login_error(request):
    return render(request, 'loginerror.html')

def buscaReceitaAprendiz(request):
    return render(request, 'buscaReceitaAprendiz.html')


def buscaReceitaMiniChef(request):
    return render(request, 'buscaReceitaMiniChef.html')


def buscaReceitaSubChef(request):
    return render(request, 'buscaReceitaSubChef.html')


def buscaReceitaChef(request):
    return render(request, 'buscaReceitaChef.html')


def buscaReceitaConfeiteiro(request):
    return render(request, 'buscaReceitaConfeiteiro.html')


def buscaReceitaVegano(request):
    return render(request, 'buscaReceitaVegano.html')


def homeAprendiz(request):
    return render(request, 'homeAprendiz.html')


def homeMiniChef(request):
    return render(request, 'homeMiniChef.html')


def homeSubChef(request):
    return render(request, 'homeSubChef.html')


def homeChef(request):
    return render(request, 'homeChef.html')


def homeConfeiteiro(request):
    return render(request, 'homeConfeiteiro.html')


def homeVegano(request):
    return render(request, 'homeVegano.html')

def livroReceitaAprendiz(request):
    return render(request, 'livroReceitaAprendiz.html')

def livroReceitaMiniChef(request):
    return render(request, 'livroReceitaMiniChef.html')

def minhasReceitasAprendiz(request):
    return render(request, 'minhasReceitasAprendiz.html')

def minhasReceitasMiniChef(request):
    return render(request, 'minhasReceitasMiniChef.html')

def minhasReceitasSubChef(request):
    return render(request, 'minhasReceitasSubChef.html')

def minhasReceitasChef(request):
    return render(request, 'minhasReceitasChef.html')

def minhasReceitasConfeiteiro(request):
    return render(request, 'minhasReceitasConfeiteiro.html')

def minhasReceitasVegano(request):
    return render(request, 'minhasReceitasVegano.html')

def adicionarReceitaAprendiz(request):
    return render(request, 'adicionarReceitaAprendiz.html')

def adicionarReceitaMiniChef(request):
    return render(request, 'adicionarReceitaMiniChef.html')

def adicionarReceitaSubChef(request):
    return render(request, 'adicionarReceitaSubChef.html')

def adicionarReceitaChef(request):
    return render(request, 'adicionarReceitaChef.html')

def adicionarReceitaConfeiteiro(request):
    return render(request, 'adicionarReceitaConfeiteiro.html')

def adicionarReceitaVegano(request):
    return render(request, 'adicionarReceitaVegano.html')

def editarPerfilAprendiz(request):
    return render(request, 'editarPerfilAprendiz.html')

# Assinatura

def assinaturaAprendiz(request):
    return render(request, 'assinaturaAprendiz.html')


def assinaturaAprendizInfor1(request):
    return render(request, 'assinaturaAprendizInfo1.html')


def assinaturaAprendizInfor2(request):
    return render(request, 'assinaturaAprendizInfo2.html')

# Fim Assinatura


# Perfil -> Alterar Senha
def alterarSenha(request):
    if request.method == "POST":
        return render(request, 'alterarSenha.html')
    return render(request, 'alterarSenha.html')

def novaSenha(request):
    if request.method == "POST":
        pass
    return render(request, 'novaSenha.html')
def livroReceitaSubChef(request):
    return render(request, 'livroReceitaSubChef.html')

def livroReceitaChef(request):
    return render(request, 'livroReceitaChef.html')

def livroReceitaConfeiteiro(request):
    return render(request, 'livroReceitaConfeiteiro.html')

def livroReceitaVegano(request):
    return render(request, 'livroReceitaVegano.html')

def plataforma():
    pass
