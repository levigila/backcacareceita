from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        Creates and saves a CustomUser with the given username, email, and password.
        """
        if not username:
            raise ValueError('The Username must be set')
        if not email:
            raise ValueError('The Email must be set')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given username, email, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    objects = CustomUserManager()

    # Remova as relações ForeignKey para Receita, Ingredientes, e Pagamento de CustomUser
    # Mantenha os outros campos e adicione o método pode_favoritar_receita aqui
    USER_TYPES = (
        ('visitor', 'Visitante'),
        ('registered', 'Usuário Cadastrado'),
        ('premium', 'Usuário Premium'),
    )
    email = models.EmailField(unique=True)
    nome_usuario = models.CharField(max_length=100)
    ID_cadastro = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=USER_TYPES, default='visitor')
    url_imagem_perfil = models.TextField(null=True, default='')
    comentario = models.TextField(null=True, blank=True)

    @property
    def receitas_favoritas(self):
        return self.livro.receitas.count()

    def pode_favoritar_receita(self):
        if self.tipo == 'visitor':
            return False
        elif self.tipo == 'registered':
            favoritos_count = self.favoritar_set.count()
            return favoritos_count < 5
        else:
            return True

class LivroDeReceitas(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='livro')
    receitas = models.ManyToManyField('Receita')

    def __str__(self):
        return f"Livro de Receitas de {self.usuario.email}"

class Favoritar(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    receita = models.ForeignKey('Receita', on_delete=models.CASCADE, null=True)

class Receita(models.Model):
    id = models.AutoField(primary_key=True)
    nome_receita = models.TextField(default='')
    categoria_receita = models.TextField(default='')
    quantidade_pessoas = models.TextField(default='')
    quantidade_horas = models.TextField(default='')
    modo_preparo = models.TextField(default='')
    dica_receita = models.TextField(default='')
    url_audio_receita = models.TextField(default='')
    url_imagem_receita = models.TextField(default='')
    comentario = models.TextField(null=True, blank=True)


class Ingredientes(models.Model):
    nome_ingredientes = models.TextField(default='')
    tipo_ingredientes = models.TextField(default='')
   
class Pagamento(models.Model):
    metodo_pagamento = models.TextField(default='')
    status_pagamento = models.TextField(default='')
    data_de_transacao = models.DateTimeField(default=None)
    valor = models.FloatField(default=None)

class Visitante(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE, null=True)
    ingredientes = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, null=True)

class ReceitaHasIngredientes(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE, null=True)
    ingredientes = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, null=True)