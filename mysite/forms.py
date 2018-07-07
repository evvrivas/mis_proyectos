#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mysite.datos_artetronica.models import *

from django.forms import ModelForm, Textarea

class UsuariosForm(ModelForm):
	class Meta:
		model= Usuarios		
		exclude=["codigoapk","plan_tienda_activo","fecha_inicio_plan","fecha_final_plan","fecha_ingreso"]

class ProductosForm(ModelForm):

	class Meta:
		model= Productos
		widgets = {'descripcion': Textarea(attrs={'cols': 40, 'rows': 3}),}
		exclude=["id_usuario","puntuacion","precio_B","fecha_ingreso"]
	
	def __init__(self, user,nombre_tienda,*args, **kwargs):
		super(ProductosForm, self).__init__(*args, **kwargs)		
		self.fields['categoria'].queryset=Categoria.objects.filter(id_usuario=user,tienda=nombre_tienda)




class BuscarForm(ModelForm):
	class Meta:
		model= Buscar
		exclude=["id_usuario","fecha_busqueda"]


class CategoriaForm(ModelForm):
	class Meta:
		model= Categoria		
		exclude=["id_usuario","nombre_tienda"]




    
class Categoria_globalForm(ModelForm):
	class Meta:
		model= Categoria_global		
		exclude=[]

class TiendasForm(ModelForm):
	class Meta:
		model= Tiendas	
		widgets = {'descripcion': Textarea(attrs={'cols': 50, 'rows': 8}),}	
		exclude=["codigoapk","id_usuario","fecha_ingreso","n_visitas","ultimo_comentario"]


class PedidosForm(ModelForm):
	class Meta:
		model= Pedidos	
		widgets = {'descripcion': Textarea(attrs={'cols': 40, 'rows': 6}),}
		exclude=["id_usuario"]


		
class Configuracion_sistemaForm(ModelForm):
	class Meta:
			
		model=Configuracion_sistema
		widgets = {'mensaje_bienvenida': Textarea(attrs={'cols': 30, 'rows': 3}),'respuesta': Textarea(attrs={'cols': 30, 'rows': 3}),}
		exclude=[]
		
