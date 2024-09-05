from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_alta = models.DateField("Fecha de publicacion")
    fecha_nacimiento = models.DateField("Fecha de nacimiento", default='1955-01-01')
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"