# Generated by Django 5.0.2 on 2024-05-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_favoritar_ingredientes_pagamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='quantidade_horas',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='receita',
            name='quantidade_pessoas',
            field=models.IntegerField(default=0),
        ),
    ]
