from django.urls import path
from .views import *
from main.views import robots_txt
from . import views 

urlpatterns = [
    path('', home, name='home'),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('chat/opciones/', opciones, name='opciones'),
    path('cookie-policy/', views.cookie_policy, name='cookie_policy'),
    path('terms-of-use/', views.terms_of_use, name='terms_of_use'),
    path('chat/webchat/', webchat, name='webchat'),
    path('salas/amistad/', salas_amistad, name='amistad'),
    path('salas/ligar/', salas_ligar, name='ligar'),
    path('salas/mas-de-40/', salas_masde40, name='masde40'),
    path('salas/amor/', salas_amor, name='amor'),
    path('salas/paises/españa/', paises_españa, name='españa'),
    path('salas/paises/latinoamerica/', paises_latinoamerica, name='latinoamerica'),
    path('salas/relaciones/', salas_ocio, name='relaciones'),
    path('salas/paises/paraguay/', paises_paraguay, name='paraguay'),
    path('salas/paises/argentina/', paises_argentina, name='argentina'),
    path('salas/dev/', salas_dev, name='dev'),
]
