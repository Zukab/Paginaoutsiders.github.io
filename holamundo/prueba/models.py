from django.db import models
from django.utils.translation import ungettext_lazy

class categorias(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre de categoria', max_length=100, null=False,blank=False)
    estado = models.BooleanField('Categoria Activada/Categoria Desactivada', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now= False, auto_now_add= True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombre de autor', max_length=225, null=False, blank=False)
    apellidos = models.CharField('Apellido de autor', max_length=225, null=False, blank=False)
    Correo = models.EmailField('Correo Electronico', blank=False,null=False)


class Meta(models.Model):
    verbose_name = 'Autor'
    verbose_name_plural = 'Autores'

def __str__(self):
        return "{0}.{1}".format(self.apellidos, self.nombres)