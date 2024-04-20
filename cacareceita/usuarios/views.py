# from django.http import HttpResponse
# from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from django.contrib.auth import login as login_django
# # Create your views here.
#
# def cadastro (request):
#     if request.method == "GET":
#         return render(request, 'cadastro.html')
#     else:
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         senha = request.POST.get('senha')
#
#         #Faz o cadastro do usuario e verifica se o usuario é igual (repetido)
#         user = User.objects.filter(username=username).first()
#
#         if user:
#             return HttpResponse('Já existe um Usuário com esse nome. Tente outro.')
#
#     user = User.objects.create_user(username=username, email=email, password=senha)
#     user.save()
#
#     return HttpResponse('Parabéns! Seu cadastro foi realizado com sucesso!');
#
# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     else:
#         username = request.POST.get('username')
#         senha = request.POST.get('senha')
#
#         user = authenticate( username=username, password=senha)
#
#         if user:
#             login_django(request, user)
#             # return HttpResponse('Login Autenticado')
#             return render(request, template_name='home.html')
#         else:
#             # return HttpResponse('E-mail ou Senha Inválidos')
#             return HttpResponse(False)
#
# def plataforma(request):
#     if request.user.is_authenticated:
#         return HttpResponse('Plataforma')
#     return HttpResponse('Você precisa estar logado')


from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

# Check if the user already exists
        if User.objects.filter(username=username).exists():
            return HttpResponse('Já existe um usuário com esse nome. Tente outro.')

        # Create the user with hashed password
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse('Parabéns! Seu cadastro foi realizado com sucesso!')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return render(request, template_name='homeAprendiz.html')
        else:
            return render(request, 'loginerror.html')
        
def receitaAprendiz(request):
    if request.method == "GET":
        return render(request, 'ReceitaAprendiz.html')
    
def receitaSubChefe(request):
    if request.method == "GET":
        return render(request, 'ReceitaSubChefe.html')


def plataforma():
    pass

def receitaMiniChefe(request):
    if request.method == "GET":
        return render(request, 'ReceitaMiniChefe.html')
    
def receitaConfeiteiro(request):
    if request.method == "GET":
        return render(request, 'ReceitaConfeiteiro.html')
    
def receitaVegano(request):
    if request.method == "GET":
        return render(request, 'ReceitaVegano.html')
    
def receitaChefe(request):
    if request.method == "GET":
        return render(request, 'ReceitaChefe.html')


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

def plataforma():
    pass

