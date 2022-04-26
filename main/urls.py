from django.urls import path
from .views import *

urlpatterns = [
    path('',main),
    path('favicon.ico/',icon),
    path('upload/',upload),
    path('hilo/<int:id>/',hilo),
    # path('<str:codigo>/',categoria),  
]
