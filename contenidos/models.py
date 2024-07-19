from django.db import models
import datetime

# modelos de Contenidos de la Aplicacion
class Consejos(models.Model):
    nombreRed= models.CharField(max_length=50)
    desarrollo= models.CharField(max_length=300)
    nombreAutor=models.CharField(max_length=80)
    
    class Meta:
        verbose_name = "Consejo"
        verbose_name_plural = "Consejos"
            
    
    def __str__(self):
        return f"{self.nombreRed}, {self.nombreAutor}"



class Musica(models.Model):
    fecha= models.DateField(default=datetime.date.today)
    artista= models.CharField(max_length=50)
    titulo= models.CharField(max_length=80)
    estilo=models.CharField(max_length=80)
    
    class Meta:
        verbose_name = "Música"
        verbose_name_plural = "Músicas"
        ordering =["estilo"]
    
    def __str__(self):
        return f"{self.titulo}, {self.artista}"


class Herramientas(models.Model):
    nombre= models.CharField(max_length=50)
    funcion= models.CharField(max_length=300)
    link=models.URLField(max_length=255)
    
    class Meta:
        verbose_name = "Herramienta"
        verbose_name_plural = "Herramientas"
        ordering =["nombre"]
    
    def __str__(self):
        return f"{self.nombre}"
    
    
class Profesionales(models.Model):
    profesion= models.CharField(max_length=50)
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    telefono= models.IntegerField()
    mail=models.EmailField()
    
    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"
        ordering =["profesion"]
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    