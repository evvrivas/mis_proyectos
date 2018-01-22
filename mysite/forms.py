#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mysite.datos_artetronica.models import *

from django.forms import ModelForm, Textarea

class UsuariosForm(ModelForm):
	class Meta:
		model= Usuarios		
		exclude=[]

class ProductosForm(ModelForm):
	class Meta:
		model= Productos
		widgets = {'descripcion': Textarea(attrs={'cols': 40, 'rows': 3}),}
		exclude=["id_usuario","puntuacion","fecha_ingreso"]

class BuscarForm(ModelForm):
	class Meta:
		model= Buscar		
		exclude=["id_usuario"]


class CategoriaForm(ModelForm):
	class Meta:
		model= Categoria		
		exclude=[]

class TiendasForm(ModelForm):
	class Meta:
		model= Tiendas		
		exclude=[]


class PedidosForm(ModelForm):
	class Meta:
		model= Pedidos	
		widgets = {'descripcion': Textarea(attrs={'cols': 40, 'rows': 6}),}
		exclude=["id_usuario","fecha_ingreso"]

class MensajesForm(ModelForm):
	class Meta:
		exclude = ('id_usuario',)		
		model=Mensajes
		widgets = {'mensaje': Textarea(attrs={'cols': 30, 'rows': 3}),'respuesta': Textarea(attrs={'cols': 30, 'rows': 3}),}
