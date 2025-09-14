from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=100, default='', )
    sobrenome = models.CharField(max_length=100, default='')
    cpf = models.CharField(max_length=11, default='')
    rg = models.CharField(max_length=12, default='')
    email = models.EmailField(unique=True, default='')
    senha = models.CharField(default='')

    def __str__(self):
        return self.nome