from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    Categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    nombre= models.CharField(max_length=200)
    precio =models.DecimalField(max_digits=6, decimal_places=2)
    stock =models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos', blank=True, null=True)
    descripcion = models.TextField( blank=True)
    pub_date =models.DateTimeField('date published')

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos =models.CharField(max_length=200)
    dni =models.CharField(max_length=200)
    telefono =models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    fehca_n=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre, self.apellidos