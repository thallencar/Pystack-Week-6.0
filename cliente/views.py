from django.shortcuts import render
from eventos.models import Certificado
from eventos.models import Evento

def meus_certificados(request):
    certificados = Certificado.objects.filter(participante=request.user)
    return render(request, 'meus_certificados.html', {'certificados': certificados})

def meus_eventos(request):
    evento = Certificado.objects.filter(participante=request.user)
    return render(request, 'meus_eventos.html', {'evento': evento})



