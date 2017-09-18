from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=150)
    descricacao = models.CharField(max_length=256)

class compromissos(models.Model):
    descricacao = models.CharField(max_length=256)

class Agendas(models.Model):
    usuario = models.ForeignKey(Usuario)

class AgendaInstitucional(Agendas):
    compromisso = models.ForeignKey(Compromissos, null=True, blank=False)

class AgendaPublica(Agendas):
    compromisso = models.ForeignKey(Compromissos, null=True, blank=False)

class AgendaPrivada(Agendas):
    compromisso = models.ForeignKey(Compromissos, null=True, blank=False)
    def __init__(self, usuario, comprimisso):
        self.usuario = usuario
        self. compromisso = compromisso

    def __str__(self):
        return self.usuario.nome
