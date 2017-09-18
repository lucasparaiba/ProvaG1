from django.shortcuts import render
from eventos.models import *
from django.http import HttpResponse
def listaAgenda(request):
    retorno = "<h1>Agendas</h1>"
    lista = Agendas.objects.all()
    for Agendas in lista:
        retorno += '</br>Agenda: {}</br>'.format(Agendas.usuario.nome)
    return HttpResponse(retorno)

def get_evento_byID(request,id):
    retorno = "<h1>Agendas</h1>"
    evento = Agendas.objects.get(pk=id)
    retorno += '</br>Agenda: {}</br>'.format(Agendas.usuario.nome)
    return HttpResponse(retorno)

def listaAgendainstirucional(request):
    retorno = "<h1>Agenda Instituicional</h1>"
    lista = AgendaInstitucional.objects.all()
    for AgendaInstitucional in lista:
        retorno += '</br>Agenda: {}</br>'.format(AgendaInstitucional.usuario.nome)
    return HttpResponse(retorno)
# Create your views here.
