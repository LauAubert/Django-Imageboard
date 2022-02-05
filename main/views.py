from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def main(request):
    hilos = Hilo.objects.all()
    categorias = Categoria.objects.all()
    return render(request,'home.html',context={'hilos':hilos,'categorias':categorias})

def upload(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.FILES)
        hilo = Hilo(
            titulo = request.POST.get('titulo'),
            contenido = request.POST.get('contenido'),
            imagen = request.FILES['file'],
            categoria = Categoria.objects.get(codigo=request.POST.get('categ'))
        )
        hilo.save()
        return redirect(main)

def hilo(request,id):
    pass

def categoria(request,codigo):
    hilos = Hilo.objects.filter(
        categoria= Categoria.objects.get(codigo=codigo)
        )
    categorias = Categoria.objects.all()
    return render(request,'home.html',context={'hilos':hilos,'categorias':categorias})