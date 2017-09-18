from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=150)


class Compromissos(models.Model):
    descricacao = models.CharField(max_length=256)

class Agendas(models.Model):
    nome = models.CharField(max_length=128)
    descricacao = models.CharField(max_length=256)
    usuario = models.ForeignKey(Usuario)


class AgendaInstitucional(Agendas):
    compromisso = models.ForeignKey(Compromissos, null=True, blank=False)

class AgendaPublica(Agendas):
    compromisso = models.ForeignKey(Compromissos, null=True, blank=False)

class AgendaPrivada(Agendas):
    compromisso = models.ForeignKey(Compromissos, null=True, blank=False)
    def __init__(self, nome, descricao, usuario):
        self.nome = nome
        self.descricao = descricao
        self.usuario = usuario

    def __str__(self):
        return self.nome
