#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mysite.datos_artetronica.models import *

from django.forms import ModelForm, Textarea

class UsuariosForm(ModelForm):
	class Meta:
		model= Usuarios		
		exclude=["codigoapk","plan_tienda_activo","fecha_ingreso"]

class ProductosForm(ModelForm):
	class Meta:
		model= Productos
		widgets = {'descripcion': Textarea(attrs={'cols': 40, 'rows': 3}),}
		exclude=["id_usuario","puntuacion","fecha_ingreso"]
	
	def __init__(self, id_usuario. *args, **kwars):
		super(ProductosForm, self).__init(*args,**kwargs)
		self.fields['categoria'].queryset=Category.objects.filter(id_usuario=request.user.username)


class BuscarForm(ModelForm):
	class Meta:
		model= Buscar		f
		exclude=["id_usuario"]


class CategoriaForm(ModelForm):
	class Meta:
		model= Categoria		
		exclude=["id_usuario"]

class Categoria_globalForm(ModelForm):
	class Meta:
		model= Categoria_global		
		exclude=[]

class TiendasForm(ModelForm):
	class Meta:
		model= Tiendas		
		exclude=["codigoapk","id_usuario","fecha_ingreso"]


class PedidosForm(ModelForm):
	class Meta:
		model= Pedidos	
		widgets = {'descripcion': Textarea(attrs={'cols': 40, 'rows': 6}),}
		exclude=["id_usuario"]

class MensajesForm(ModelForm):
	class Meta:
		exclude = ('id_usuario',)		
		model=Mensajes
		widgets = {'mensaje': Textarea(attrs={'cols': 30, 'rows': 3}),'respuesta': Textarea(attrs={'cols': 30, 'rows': 3}),}


		
