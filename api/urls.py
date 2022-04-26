from django.urls import path
from .views import *

urlpatterns = [
    path('threads/', threads),
    path('category/',category),
    path('thread/<str:code>',thread),
    path('thread/<str:code>/comm/',threadComments)
]
