from dataclasses import fields
from main.models import *
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.crypto import get_random_string
# from .models import *
from django.core import serializers
import json
# Create your views here.
def threads(request):
    if request.method == 'GET':
        see,offset = 20 , 0
        try:    offset = int(request.GET.get('offset'))
        except: pass 
        print(see,offset)
        threads_raw = serializers.serialize('python',Hilo.objects.all()[offset:see+offset])     # serializo todo
        threads = [d['fields'] for d in threads_raw]                                            # lo formateo bien
        for d in threads: 
            d.pop('usuario',None)
            d.pop('contenido',None)
        threads = [serialFecha(d,['fecha_creacion','fecha_actualizado']) for d in threads]      # formateo las fechas



        return HttpResponse(json.dumps(threads))
def category(request):pass
def thread(request):pass
def threadComments(request):pass

