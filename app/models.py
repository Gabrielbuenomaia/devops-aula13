"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    periodo = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=200)

class Vestibular(models.Model):
    nome = models.CharField(max_length=200)
    
class candidatos(models.Model):
    nome = models.CharField(max_length=200)
    RG = models.CharField(max_length=50)
    CPF = models.CharField(max_length=200)    

