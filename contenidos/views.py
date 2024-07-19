from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def home (request):
    return render(request, "contenidos/index.html")
def acerca (request):
    return render(request, "contenidos/acerca.html")

#__ Categoria de contenido CONSEJOS
@login_required
def consejos (request):
    contexto = {"consejos": Consejos.objects.all()}
    return render(request, "contenidos/consejos.html", contexto)

@login_required
def consejosForm(request):
    if request.method == "POST":
        miForm=ConsejosForm(request.POST)
        if miForm.is_valid():
            consejo_nombreRed=miForm.cleaned_data.get("nombreRed")
            consejo_desarrollo=miForm.cleaned_data.get("desarrollo")
            consejo_nombreAutor=miForm.cleaned_data.get("nombreAutor")
            consejo=Consejos(nombreRed=consejo_nombreRed, desarrollo=consejo_desarrollo, nombreAutor=consejo_nombreAutor)
            consejo.save()
            contexto = {"consejos": Consejos.objects.all()}
            return render(request, "contenidos/consejos.html", contexto)
    else:
       miForm = ConsejosForm()
       
    return render(request, "contenidos/consejosForm.html",{"form":miForm}) 

@login_required
def buscarConsejos(request):
    return render(request, "contenidos/buscarConsejos.html")

@login_required
def encontrarConsejos(request):
    if request.GET["buscarConsejos"]:
        patron= request.GET["buscarConsejos"]
        consejos= Consejos.objects.filter(nombreRed__icontains=patron)
        contexto={"consejos":consejos}
    else:
        contexto={"consejos": Consejos.objects.all()}
    
    return render(request, "contenidos/consejos.html", contexto)

@login_required
def consejoUpdate(request, idConsejo):
    consejo= Consejos.objects.get(id=idConsejo)
    if request.method == "POST":
        miForm=ConsejosForm(request.POST)
        if miForm.is_valid():
            consejo.nombreRed=miForm.cleaned_data.get("nombreRed")
            consejo.desarrollo=miForm.cleaned_data.get("desarrollo")
            consejo.nombreAutor=miForm.cleaned_data.get("nombreAutor")
            consejo.save()
            contexto = {"consejos": Consejos.objects.all()}
            return render(request, "contenidos/consejos.html", contexto)
    else:
        miForm = ConsejosForm(initial={"nombreRed":consejo.nombreRed, "desarrollo":consejo.desarrollo, "nombreAutor":consejo.nombreAutor})

    return render (request, "contenidos/consejosForm.html",{"form":miForm})

@login_required
def consejoDelete(request, idConsejo):
    consejo= Consejos.objects.get(id=idConsejo)
    consejo.delete()
    contexto = {"consejos": Consejos.objects.all()}
    return render(request, "contenidos/consejos.html", contexto)


#__ Categoria de contenido MUSICA

@login_required
def musica (request):
    contexto = {"musica": Musica.objects.all()}
    return render(request, "contenidos/musica.html", contexto)

@login_required
def musicaForm(request):
    if request.method == "POST":
        miForm=MusicaForm(request.POST)
        if miForm.is_valid():
                       
            musica_artista=miForm.cleaned_data.get("artista")
            musica_titulo=miForm.cleaned_data.get("titulo")
            musica_estilo=miForm.cleaned_data.get("estilo")
            musica=Musica(artista=musica_artista, titulo=musica_titulo, estilo=musica_estilo )
            musica.save()
            contexto = {"musica": Musica.objects.all()}
            return render(request, "contenidos/musica.html", contexto)
    else:
       miForm = MusicaForm()
       
    return render(request, "contenidos/musicaForm.html",{"form":miForm}) 

@login_required
def musicaUpdate(request, idMusica):
    musica= Musica.objects.get(id=idMusica)
    if request.method == "POST":
        miForm=MusicaForm(request.POST)
        if miForm.is_valid():
            musica.artista=miForm.cleaned_data.get("artista")
            musica.titulo=miForm.cleaned_data.get("titulo")
            musica.estilo=miForm.cleaned_data.get("estilo")
            musica.save()
            contexto = {"musica": Musica.objects.all()}
            return render(request, "contenidos/musica.html", contexto)
    else:
        miForm = MusicaForm(initial={"artista": musica.artista, "titulo": musica.titulo, "estilo": musica.estilo})

    return render (request, "contenidos/musicaForm.html",{"form":miForm})

@login_required
def musicaDelete(request, idMusica):
    musica= Musica.objects.get(id=idMusica)
    musica.delete()
    contexto = {"musica": Musica.objects.all()}
    return render(request, "contenidos/musica.html", contexto)


    
#__ Categoria de contenido HERRAMIENTAS

class HerramientasList(LoginRequiredMixin, ListView):
    model = Herramientas
    
class HerramientasCreate(LoginRequiredMixin, CreateView):
    model = Herramientas
    fields = ["nombre", "funcion", "link"]
    success_url= reverse_lazy("herramientas")
    
class HerramientasUpdate(LoginRequiredMixin, UpdateView):
    model = Herramientas
    fields = ["nombre", "funcion", "link"]
    success_url= reverse_lazy("herramientas")
    
class HerramientasDelete(LoginRequiredMixin, DeleteView):
    model = Herramientas
    success_url= reverse_lazy("herramientas")


#__ Categoria de contenido PROFESIONALES

class ProfesionalesList(LoginRequiredMixin, ListView):
    model = Profesionales
    
class ProfesionalesCreate(LoginRequiredMixin, CreateView):
    model = Profesionales
    fields = ["profesion", "nombre", "apellido", "telefono", "mail"]
    success_url= reverse_lazy("profesionales")
    
class ProfesionalesUpdate(LoginRequiredMixin, UpdateView):
    model = Profesionales
    fields = ["profesion", "nombre", "apellido", "telefono", "mail"]
    success_url= reverse_lazy("profesionales")
    
class ProfesionalesDelete(LoginRequiredMixin, DeleteView):
    model = Profesionales
    success_url= reverse_lazy("profesionales")
    

#__ Login / Logout / Registration

def loginUsuario(request):
    if request.method == "POST":
        usuario = request.POST ["username"]
        clave = request.POST ["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request,user)
            return render(request,"contenidos/index.html")
        else:
            return redirect (reverse_lazy('login'))
    
    else:
        miForm = AuthenticationForm()
        
    return render(request, "contenidos/login.html", {"form": miForm})

def registroUsuario (request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid() :
            miForm.save()
            return redirect (reverse_lazy('home'))
    
    else:
        miForm = RegistroForm()
        
    return render(request, "contenidos/registro.html", {"form": miForm})
