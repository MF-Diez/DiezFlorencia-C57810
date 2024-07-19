from django.urls import path, include
from contenidos.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',home, name="home"),
    path('index/',home, name="home"),
    
    path('acerca/',acerca, name="acerca"),
    
#__ Login / logout / registration 
    path('login/',loginUsuario, name="login"),
    path('logout/', LogoutView.as_view(template_name='contenidos/logout.html'), name='logout'),
    path('registro/',registroUsuario, name="registro"),
    
#__ Categoria de contenido CONSEJOS
    path('consejos/',consejos, name="consejos"),
    path('consejosForm/',consejosForm, name="consejosForm"),
    path('buscarConsejos/',buscarConsejos, name="buscarConsejos"),
    path('encontrarConsejos/',encontrarConsejos, name="encontrarConsejos"),
    path('consejoUpdate/<idConsejo>/',consejoUpdate, name="consejoUpdate"),
    path('consejoDelete/<idConsejo>/',consejoDelete, name="consejoDelete"),
    
#__ Categoria de contenido MUSICA
    path('musica/',musica, name="musica"),
    path('musicaForm/',musicaForm, name="musicaForm"),
    path('musicaUpdate/<idMusica>/',musicaUpdate, name="musicaUpdate"),
    path('musicaDelete/<idMusica>/',musicaDelete, name="musicaDelete"),
    
#__ Categoria de contenido HERRRAMIENTAS
    path('herramientas/',HerramientasList.as_view(), name="herramientas"),
    path('herramientasCreate/',HerramientasCreate.as_view(), name="herramientasCreate"),
    path('herramientasUpdate/<int:pk>/',HerramientasUpdate.as_view(), name="herramientasUpdate"),
    path('herramientasDelete/<int:pk>/',HerramientasDelete.as_view(), name="herramientasDelete"),

    
#__ Categoria de contenido PROFESIONALES
    path('profesionales/',ProfesionalesList.as_view(), name="profesionales"),
    path('profesionalesCreate/',ProfesionalesCreate.as_view(), name="profesionalesCreate"),
    path('profesionalesUpdate/<int:pk>/',ProfesionalesUpdate.as_view(), name="profesionalesUpdate"),
    path('profesionalesDelete/<int:pk>/',ProfesionalesDelete.as_view(), name="profesionalesDelete"),
]
