#encoding:utf-8
from django.db import models

# Create your models here.

class Cliente(models.Model):
        nombre=models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	direccion=models.CharField(max_length=100)
        telefono=models.IntegerField(max_length=20)
	correo=models.EmailField(max_length=75)
        def __unicode__(self):
	    return self.nombre

class Canasta(models.Model):
	cliente=models.ForeignKey(Cliente)
        fecha=models.DateField()
        subtotal=models.FloatField(max_length=15)
	total=models.FloatField(max_length=15)
        iva=models.FloatField(max_length=15)
        def __unicode__(self):
	    return self.fecha

class Item(models.Model):
        descripcion=models.CharField(max_length=100)
        precio=models.FloatField(max_length=15)
        def __unicode__(self):
	    return self.descripcion

class ItemCanasta(models.Model):
	item=models.ForeignKey(Item)
	canasta=models.ForeignKey(Canasta)
	cantidad=models.IntegerField(max_length=15)
        def __unicode__(self):
	    return self.cantidad

class Categoria(models.Model):
	item=models.ForeignKey(Item)
	categoria=models.CharField(max_length=50)
        def __unicode__(self):
	    return self.categoria

class CategoriaProducto(models.Model):
	item=models.ForeignKey(Item)
	categoria=models.ForeignKey(Categoria)


