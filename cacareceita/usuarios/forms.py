from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class RegistroForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'nome_usuario', 'ID_cadastro', 'tipo']
    
    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("password1")
        confirma_senha = cleaned_data.get("password2")
        if senha and confirma_senha and senha != confirma_senha:
            raise forms.ValidationError("As senhas não coincidem.")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    senha = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        senha = cleaned_data.get("senha")
        
        # Adicione validações personalizadas aqui, como verificar se o usuário existe no sistema, etc.
