from operator import mod
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    codigo = models.CharField(max_length=4)

    def __str__(self) -> str:
        return f'{self.codigo} - {self.nombre}'
    class Meta:
        ordering = ['nombre']

class Hilo(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.TextField()
    # usuario
    imagen = models.ImageField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # fecha creacion
    # fecha actualizado

# class comentario
    # usuario
    # hilo
    # fecha
    # contenido
    # 
