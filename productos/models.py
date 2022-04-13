from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)

    class Meta:
        db_table = 'categorias'

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    short_description = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    imagen = models.ImageField()
    disponible = models.BooleanField(default=True, null=False)
    precio = models.FloatField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        db_table = 'productos'


