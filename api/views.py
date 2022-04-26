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
        ser_hilo = SerializadorHilo()
        threads = ser_hilo.serialize(Hilo.objects.all()[offset:see+offset])
        return HttpResponse(json.dumps(threads))

def category(request):pass
def thread(request,code):
    thread = Hilo.objects.get(codigo=code)
    ser_hilo = SerializadorHilo()
    thread = ser_hilo.serialize([thread])
    return HttpResponse(json.dumps(thread))

def threadComments(request,code):
    see = 20
    try:offset = int(request.GET.get('offset'))
    except:offset=0
    if request.method == 'GET':
        comments = Comentario.objects.filter(
            hilo=Hilo.objects.get(codigo=code)) [offset:offset+see]
        ser_comm = SerializadorComentario()
        comments = ser_comm.serialize(comments)
        
    return HttpResponse(json.dumps(comments))

class SerializadorHilo(serializers.get_serializer('python')):
    def serialize(self,obj):
        threads = super().serialize(obj)
        threads = [d['fields'] for d in threads]
        # print('Largo Ser: ',len(obj))
        for d in threads: 
            if len(obj) >1:d.pop('contenido',None)
            d.pop('usuario',None)            
        threads = [serialFecha(d,['fecha_creacion','fecha_actualizado']) for d in threads]
        return threads
    
class SerializadorComentario(serializers.get_serializer('python')):
    def serialize(self,obj):
        comments = super().serialize(obj,use_natural_foreign_keys=True)
        comments = [d['fields'] for d in comments]
        for comment in comments:
            comment.pop('usuario',None)
            comment['respuestas'] = comment['respuestas'].split('-')
            if comment['respuestas'][0] == '':comment['respuestas'].pop()
        comments = [serialFecha(d,['fecha']) for d in comments]
        return comments


