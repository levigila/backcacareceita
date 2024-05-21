from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import CustomUser
from .models import CustomUserManager
from django.contrib.auth import authenticate, login as login_django, logout
from django.urls import reverse
from .forms import RegistroForm, LoginForm  # Importando o novo formulário
from spoonacular.api import API
from django.conf import settings
from .models import Receita
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# from .utils import translate_text
from .utils import get_recipes_meals
# from google.cloud import translate_v2 as translate
import requests

client = API(api_key='030af2ba4b0b4a36b82f165e979d4f44')

def home_aprendiz(request):
    meal_types = ['appetizer', 'salad', 'side dish', 'beverage']
    recipes = get_recipes_meals(meal_types)
    return render(request, 'home_aprendiz.html', {'recipes': recipes})
    


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

@login_required
@require_POST
@csrf_exempt
def favoritar_receita(request):
    if request.method == 'POST' and request.user.is_authenticated:
        data = JsonResponse.loads(request.body)
        receita_id = data.get('receita_id')
        try:
            receita = Receita.objects.get(api_id=receita_id)
            user = request.user
            user.livro.receitas.add(receita)
            return JsonResponse({'success': True})
        except Receita.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Receita não encontrada'})
    return JsonResponse({'success': False, 'error': 'Requisição inválida'})

def pesquisarReceita(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        client = API(api_key=settings.SPOOONACULAR_API_KEY)
        receita = client.search_recipes_by_ingredients(ingredients=query)
        context = {'receita': receita}
        return render(request, 'search_results.html', context)
    
def search_recipes(request):
    api_key = '030af2ba4b0b4a36b82f165e979d4f44'  # Substitua pela sua chave de API da Spoonacular
    ingredients = request.GET.get('ingredients', '')
    url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=12&apiKey={api_key}'
    response = requests.get(url)
    recipes = response.json()
    translated_recipes = []
    for recipe in recipes:
        translated_title = translate_text(recipe['title'], target_language='pt')
        translated_recipes.append({
            'id': recipe['id'],
            'title': translated_title,
            'image': recipe['image'],
            'missedIngredientCount': recipe['missedIngredientCount']
        })
    
    # Certifique-se de retornar uma resposta JSON
    return JsonResponse(translated_recipes, safe=False)

def detalhes_receita(request, id_receita):
    api_key = '030af2ba4b0b4a36b82f165e979d4f44'
    url = f'https://api.spoonacular.com/recipes/{id_receita}/information?apiKey={api_key}'
    response = requests.get(url)
    receita = response.json()

    return render(request, 'receitaAprendiz.html', {'receita': receita})

def traduzir_texto(texto, target_language='pt'):
    translate_client = translate.Client()
    resultado = translate_client.translate(texto, target_language=target_language)
    return resultado['translatedText']

def receitaAprendiz(request):
    recipe_id = request.GET.get('id', '')  # Obtém o ID da receita a partir da URL
    return render(request, 'receitaAprendiz.html', {'recipe_id': recipe_id})


def receitaSubChef(request, receita_id):
    if request.method == 'GET':
        # Use Spoonacular to get recipe details
        receita = client.get_recipe_by_id(id=receita_id)

        # Check if recipe exists and belongs to the Sub Chef cuisine category
        if receita and receita['cuisine'] == "Sub Chef":
            # Process and format recipe data
            context = {'receita': receita}
            return render(request, 'receitaSubChef.html', context)
        else:
            return render(request, 'receitaSubChef.html', {'erro': 'Receita não encontrada ou não pertence à categoria Sub Chef'})
    else:
        return render(request, 'receitaSubChef.html')


def receitaMiniChef(request, receita_id):
    if request.method == 'GET':
        # Use Spoonacular to get recipe details
        receita = client.get_recipe_by_id(id=receita_id)

        # Check if recipe exists and belongs to the Mini Chef cuisine category
        if receita and receita['cuisine'] == "Mini Chef":
            # Process and format recipe data
            context = {'receita': receita}
            return render(request, 'receitaMiniChef.html', context)
        else:
            return render(request, 'receitaMiniChef.html', {'erro': 'Receita não encontrada ou não pertence à categoria Mini Chef'})
    else:
        return render(request, 'receitaMiniChef.html')


def receitaConfeiteiro(request, receita_id):
    if request.method == 'GET':
        # Use Spoonacular to get recipe details
        receita = client.get_recipe_by_id(id=receita_id)

        # Check if recipe exists and belongs to the Confeiteiro cuisine category
        if receita and receita['cuisine'] == "Confeiteiro":
            # Process and format recipe data
            context = {'receita': receita}
            return render(request, 'receitaConfeiteiro.html', context)
        else:
            return render(request, 'receitaConfeiteiro.html', {'erro': 'Receita não encontrada ou não pertence à categoria Confeiteiro'})
    else:
        return render(request, 'receitaConfeiteiro.html')



def receitaVegano(request, receita_id):
    if request.method == 'GET':
        # Use Spoonacular to get recipe details
        receita = client.get_recipe_by_id(id=receita_id)

        # Check if recipe exists and belongs to the Vegano diet category
        if receita and receita['diets'] == ["Vegan"]:
            # Process and format recipe data
            context = {'receita': receita}
            return render(request, 'receitaVegano.html', context)
        else:
            return render(request, 'receitaVegano.html', {'erro': 'Receita não encontrada ou não pertence à categoria Vegano'})
    else:
        return render(request, 'receitaVegano.html')



def receitaChef(request, receita_id):
    if request.method == 'GET':
        # Use Spoonacular to get recipe details
        receita = client.get_recipe_by_id(id=receita_id)

        # Check if recipe exists and belongs to the Chef cuisine category
        if receita and receita['cuisine'] == "Chef":
            # Process and format recipe data
            context = {'receita': receita}
            return render(request, 'receitaChef.html', context)
        else:
            return render(request, 'receitaChef.html', {'erro': 'Receita não encontrada ou não pertence à categoria Chef'})
    else:
        return render(request, 'receitaChef.html')



def login_error(request):
    return render(request, 'loginerror.html')


def buscaReceitaAprendiz(request):
    return render(request, 'buscaReceitaAprendiz.html')


def buscaReceitaMiniChef(request):
    if request.method == 'GET':
        termo_busca = request.GET.get('termo_busca')
        if termo_busca:
            # Use Spoonacular to search for recipes
            receitas = client.search_recipes(query=termo_busca)

            # Filter results to exclude Mini Chef recipes
            mini_chef_excluidas = []
            for receita in receitas:
                if receita['cuisine'] != "Mini Chef":
                    mini_chef_excluidas.append(receita)

            context = {'receitas': mini_chef_excluidas}
            return render(request, 'buscaReceitaMiniChef.html', context)
        else:
            return render(request, 'buscaReceitaMiniChef.html')
    else:
        return render(request, 'buscaReceitaMiniChef.html') 


def buscaReceitaSubChef(request):
    if request.method == 'GET':
        termo_busca = request.GET.get('termo_busca')
        if termo_busca:
            # Use Spoonacular to search for recipes
            receitas = client.search_recipes(query=termo_busca)

            # Filter results to include Sub Chef recipes
            subchef_receitas = []
            for receita in receitas:
                if receita['cuisine'] == "Sub Chef":
                    subchef_receitas.append(receita)

            context = {'receitas': subchef_receitas}
            return render(request, 'buscaReceitaSubChef.html', context)
        else:
            return render(request, 'buscaReceitaSubChef.html')
    else:
        return render(request, 'buscaReceitaSubChef.html')


def buscaReceitaChef(request):
    if request.method == 'GET':
        termo_busca = request.GET.get('termo_busca')
        if termo_busca:
            # Use Spoonacular to search for recipes
            receitas = client.search_recipes(query=termo_busca, cuisine=["Chef"])

            # Filter results to only include Chef recipes
            chef_receitas = []
            for receita in receitas:
                if receita['cuisine'] == "Chef":
                    chef_receitas.append(receita)

            context = {'receitas': chef_receitas}
            return render(request, 'buscaReceitaChef.html', context)
        else:
            return render(request, 'buscaReceitaChef.html')
    else:
        return render(request, 'buscaReceitaChef.html')



def buscaReceitaConfeiteiro(request):
    if request.method == 'GET':
        termo_busca = request.GET.get('termo_busca')
        if termo_busca:
            # Use Spoonacular to search for recipes
            receitas = client.search_recipes(query=termo_busca)

            # Filter results to include Confeiteiro recipes
            confeiteiro_receitas = []
            for receita in receitas:
                if receita['cuisine'] == "Confeiteiro":
                    confeiteiro_receitas.append(receita)

            context = {'receitas': confeiteiro_receitas}
            return render(request, 'buscaReceitaConfeiteiro.html', context)
        else:
            return render(request, 'buscaReceitaConfeiteiro.html')
    else:
        return render(request, 'buscaReceitaConfeiteiro.html')



def buscaReceitaVegano(request):
    if request.method == 'GET':
        termo_busca = request.GET.get('termo_busca')
        if termo_busca:
            # Use Spoonacular to search for recipes
            receitas = client.search_recipes(query=termo_busca)

            # Filter results to include Vegano recipes
            vegano_receitas = []
            for receita in receitas:
                if receita['diets'] == ["Vegan"]:
                    vegano_receitas.append(receita)

            context = {'receitas': vegano_receitas}
            return render(request, 'buscaReceitaVegano.html', context)
        else:
            return render(request, 'buscaReceitaVegano.html')
    else:
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

def editarPerfilMiniChef(request):
    return render(request, 'editarPerfilMiniChef.html')

def editarPerfilSubChef(request):
    return render(request, 'editarPerfilSubChef.html')

def editarPerfilChef(request):
    return render(request, 'editarPerfilChef.html')

def editarPerfilConfeiteiro(request):
    return render(request, 'editarPerfilConfeiteiro.html')

def editarPerfilVegano(request):
    return render(request, 'editarPerfilVegano.html')

# Assinatura

def assinaturaAprendiz(request):
    return render(request, 'assinaturaAprendiz.html')


def assinaturaAprendizInfor1(request):
    return render(request, 'assinaturaAprendizInfo1.html')


def assinaturaAprendizInfor2(request):
    return render(request, 'assinaturaAprendizInfo2.html')

def assinaturaAprendizFinalizada(request):
    return render(request, 'assinaturaAprendizFinalizada.html')
#

def assinaturaMiniChef(request):
    return render(request, 'assinaturaMiniChef.html')


def assinaturaMiniChefInfor1(request):
    return render(request, 'assinaturaMiniChefInfo1.html')


def assinaturaMiniChefInfor2(request):
    return render(request, 'assinaturaMiniChefInfo2.html')

def assinaturaMiniChefFinalizada(request):
    return render(request, 'assinaturaMiniChefFinalizada.html')
#

def assinaturaSubChef(request):
    return render(request, 'assinaturaSubChef.html')


def assinaturaSubChefInfor1(request):
    return render(request, 'assinaturaSubChefInfo1.html')


def assinaturaSubChefInfor2(request):
    return render(request, 'assinaturaSubChefInfo2.html')

def assinaturaSubChefFinalizada(request):
    return render(request, 'assinaturaSubChefFinalizada.html')
#

def assinaturaChef(request):
    return render(request, 'assinaturaChef.html')


def assinaturaChefInfor1(request):
    return render(request, 'assinaturaChefInfo1.html')


def assinaturaChefInfor2(request):
    return render(request, 'assinaturaChefInfo2.html')

def assinaturaChefFinalizada(request):
    return render(request, 'assinaturaChefFinalizada.html')
#

def assinaturaConfeiteiro(request):
    return render(request, 'assinaturaConfeiteiro.html')


def assinaturaConfeiteiroInfor1(request):
    return render(request, 'assinaturaConfeiteiroInfo1.html')


def assinaturaConfeiteiroInfor2(request):
    return render(request, 'assinaturaConfeiteiroInfo2.html')

def assinaturaConfeiteiroFinalizada(request):
    return render(request, 'assinaturaConfeiteiroFinalizada.html')
#

def assinaturaVegano(request):
    return render(request, 'assinaturaVegano.html')


def assinaturaVeganoInfor1(request):
    return render(request, 'assinaturaVeganoInfo1.html')


def assinaturaVeganoInfor2(request):
    return render(request, 'assinaturaVeganoInfo2.html')

def assinaturaVeganoFinalizada(request):
    return render(request, 'assinaturaVeganoFinalizada.html')

# Fim Assinatura

#Editar receita
def editarReceitaAprendiz(request):
    return render(request, 'editarReceitaAprendiz.html')

def editarReceitaMiniChef(request):
    return render(request, 'editarReceitaMiniChef.html')

def editarReceitaSubChef(request):
    return render(request, 'editarReceitaSubChef.html')

def editarReceitaChef(request):
    return render(request, 'editarReceitaChef.html')

def editarReceitaConfeiteiro(request):
    return render(request, 'editarReceitaConfeiteiro.html')

def editarReceitaVegano(request):
    return render(request, 'editarReceitaVegano.html')

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
