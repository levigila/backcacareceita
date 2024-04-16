from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_set',  # Adicione este related_name para evitar conflitos
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set',  # Adicione este related_name para evitar conflitos
        related_query_name='user',
    )   

    USER_TYPES = (
        ('visitor', 'Visitante'),
        ('registered', 'Usuário Cadastrado'),
        ('premium', 'Usuário Premium'),
    )
    email = models.EmailField(unique=True)
    nome_usuario = models.CharField(max_length=100)
    ID_cadastro = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=USER_TYPES, default='visitor')

    def _str_(self):
        return self.email

class Receita(models.Model):
    id_receita = models.AutoField(primary_key=True)
    nome_receita = models.CharField(max_length=100)
    descricao = models.TextField()
    modo_de_preparo = models.TextField()
    avaliacao = models.FloatField(default=0.0)

    def _str_(self):
        return self.nome_receita

class Ingrediente(models.Model):
    id_ingredientes = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    CATEGORIA_CHOICES = (
        ('proteina', 'Proteína'),
        ('carboidrato', 'Carboidrato'),
        ('oleos_gorduras', 'Óleos/Gorduras'),
        ('carnes', 'Carnes'),
        ('vegetais', 'Vegetais'),
        ('frutas', 'Frutas'),
        ('legumes', 'Legumes'),
    )
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    unidade_de_medida = models.CharField(max_length=20)

    def _str_(self):
        return self.nome

class Alergeno(models.Model):
    ingrediente = models.OneToOneField(Ingrediente, on_delete=models.CASCADE, related_name='alergenos')
    glúten = models.BooleanField(default=False)
    lactose = models.BooleanField(default=False)
    nozes = models.BooleanField(default=False)
    # Adicione outros alérgenos conforme necessário

    def _str_(self):
        return f"Alergenos de {self.ingrediente.nome}"