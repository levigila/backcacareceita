# usuarios/utils.py
import requests
from google.cloud import translate_v2 as translate

def translate_text(text, target_language='pt'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

def get_recipes_meals(meal_types):
    api_key = 'a50e2cf10f3d4ca1b044d66c63dced85'  # Substitua 'sua_api_key_aqui' pela sua chave de API Spoonacular
    url = 'https://api.spoonacular.com/recipes/complexSearch'

    params = {
        'apiKey': api_key,
        'type': ','.join(meal_types),  # Concatena os tipos de refeição em uma string separada por vírgulas
        'number': 9  # Número de receitas a serem recuperadas
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['results']  # Retorna a lista de receitas