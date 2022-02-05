from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def main(request):
    hilos = Hilo.objects.all()
    return render(request,'home.html',context={'hilos':hilos})

def upload(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.FILES)
        hilo = Hilo(
            titulo = request.POST.get('titulo'),
            contenido = request.POST.get('contenido'),
            imagen = request.FILES['file'],
            categoria = Categoria.objects.get(codigo='ECO')
        )
        hilo.save()
        return redirect(main)