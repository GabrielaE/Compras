#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import Cliente, Canasta, Item, ItemCanasta, Categoria, CategoriaProducto

class ClienteForm(ModelForm):
    class Meta:
        model=Cliente
