from django.db import models
from django.conf import settings
import datetime
from django.utils.crypto import get_random_string
import string

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
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField('creado',default=datetime.datetime.now())
    fecha_actualizado = models.DateTimeField('actualizado',default=datetime.datetime.now())
    codigo = models.CharField(max_length=20,default=get_random_string(20,
        allowed_chars=string.ascii_uppercase+string.digits),null=False)
    numero_comentarios= models.IntegerField(default=0)

    class Meta:
        ordering = ['-fecha_actualizado','titulo']
    def natural_key(self):
        return self.codigo


class Comentario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    hilo = models.ForeignKey(Hilo, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=datetime.datetime.now())
    texto = models.TextField()
    imagen = models.ImageField(blank=True)
    codigo = models.CharField(max_length=8,default=get_random_string(8,
        allowed_chars=string.ascii_uppercase+string.digits))
    respuestas = models.CharField(max_length=255, blank=True,default='')
    es_op = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha']

def serialFecha(modelo,fechas): 
    try:
        for fecha in fechas:
            modelo[fecha] = modelo[fecha].strftime('%Y-%m-%dT%H:%M:%S') # w3cdtf
    except:pass
    return  modelo

# def generarCodigo(largo):
#     lista = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#     codigo = ''
#     for i in range(largo):
#         codigo += lista[random.randint(0,len(lista)-1)]
#     return codigo
'''
def generarCodigo(modelo,largo):
    while True:
        codigo = get_random_string(largo).upper()
        if len(modelo.objects.get(codigo=codigo))==0: break
    return codigo
'''