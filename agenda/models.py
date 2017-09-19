from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=150)
    def __str__(self):
        return self.nome + "(" + self.email + ")"

class Compromissos(models.Model):

    descricacao = models.CharField(max_length=256)
    def __str__(self):
        return self.descricacao

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
    def __str__(self):
        return self.nome
