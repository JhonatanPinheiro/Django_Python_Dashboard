from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quatidade em Estoque')

#Criando uma função STR
#Essa função str que vai apresentar o nosso objeto instaciado de acordo com que queremos
    def __str__(self):
        return  self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length = 100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'