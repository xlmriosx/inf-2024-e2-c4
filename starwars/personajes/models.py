from django.db import models

# Create your models here.
class Personaje(models.Model):
    alias = models.CharField(max_length=30)
    nombre_completo = models.CharField(max_length=30)
    casa = models.CharField(max_length=30) # Republica o imperio
    tiempo = models.CharField(max_length=30) # Previo o posterior a X guerra/tiempo
    foto = models.ImageField(upload_to='personajes/')
    # cargado_en = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.alias} {self.tiempo}"
