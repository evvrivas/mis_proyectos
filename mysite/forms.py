#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mysite.datos_artetronica.models import *

from django.forms import ModelForm, Textarea, TextInput, NumberInput




class UsuariosForm(ModelForm):
	class Meta:
		model= Usuarios		
		exclude=["codigoapk","plan_tienda_activo","fecha_inicio_plan","fecha_final_plan","fecha_ingreso"]

class ProductosForm(ModelForm):

	class Meta:
		model= Productos
		widgets = {'descripcion': Textarea(attrs={'cols': 30, 'rows': 2}),}
		exclude=["id_usuario","puntuacion","fecha_ingreso","ultima_fecha_edicion"]
	
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
		widgets = {'descripcion': Textarea(attrs={'cols': 30, 'rows': 2}),}			
		exclude=["id_usuario","tienda"]

    
#class Categoria_globalForm(ModelForm):
#	class Meta:
#		model= Categoria_global		
#		exclude=[]

class TiendasForm(ModelForm):
	class Meta:
		model= Tiendas	
		widgets = {'descripcion': Textarea(attrs={'cols': 30, 'rows': 2}),}	
		exclude=["tipo_de_vista","codigoapk","id_usuario","fecha_ingreso","n_visitas","ultimo_comentario","ultima_fecha_edicion"]
	def __init__(self, user,*args, **kwargs):
		super(TiendasForm, self).__init__(*args, **kwargs)
		self.fields['ccomercial'].queryset=Ccomercial.objects.all()
		#self.fields['ccomercial'].queryset=Ccomercial.objects.filter(id_usuario=user)




class PedidosForm(ModelForm):
	class Meta:
		model= Pedidos	
		widgets = {'descripcion': Textarea(attrs={'cols': 30, 'rows': 3}),}
		exclude=["id_usuario"]

	
class Configuracion_sistemaForm(ModelForm):
	class Meta:
			
		model=Configuracion_sistema
		widgets = {'mensaje_bienvenida': Textarea(attrs={'cols': 30, 'rows': 2}),'respuesta': Textarea(attrs={'cols': 30, 'rows': 3}),}
		exclude=[]
		
class MensajesForm(ModelForm):
	class Meta:			
		model=Mensajes
		widgets = {'pregunta': Textarea(attrs={'cols': 20, 'rows': 2}),'respuesta': Textarea(attrs={'cols': 20, 'rows': 2}),}
		exclude=["id_usuario","fecha"]

class CcomercialForm(ModelForm):
	class Meta:			
		model=Ccomercial
		widgets = {'descripcion_ccomercial': Textarea(attrs={'cols': 30, 'rows': 2})}
		exclude=["id_usuario"]

class Carro_de_comprasForm(ModelForm):
	class Meta:			
		model=Carro_de_compras
		widgets = {'especificacion': Textarea(attrs={'cols': 20, 'rows': 2}) }

		exclude=["fecha_ingreso","id_comprador","total","estado_prod","mostrar_foto"]

		
#class Item_carroForm(ModelForm):
#	class Meta:			
#		model=Item_carro
#		widgets = {'especificacion': Textarea(attrs={'cols': 20, 'rows': 1}),}
				   #'nombre_tienda' :  TextInput(attrs={'size': 20}),
				   #'cantidad' : NumberInput(attrs={'size':'5'}),
				   #'nombre' :  TextInput(attrs={'size': 20}),
				   #'precio' :  NumberInput(attrs={'size':'5'}),
				   #'especificacion' :  TextInput(attrs={'size': 20}),
				   #'estado_prod' :  TextInput(attrs={'size': 20})
				    # }

#		exclude=[]
