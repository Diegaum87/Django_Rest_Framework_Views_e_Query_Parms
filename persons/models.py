from django.db import models

# Create your models here.
class Person(models.Model):
    name  = models.CharField(max_length=100)# nome tamanho máximo 100, obrigatório..
    cpf = models.CharField(max_length=11, unique=True)# cpf tamanho máximo 11, unico, obrigatório.
    email = models.EmailField(null=True)# email, Email obrigatório, nulo..
    birthdate = models.DateField(null=True)# birthdate, é uma data obrigatória, nulo
    married = models.BooleanField(default=False)# married é um boolean e default falso.