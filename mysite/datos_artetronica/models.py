#!/usr/bin/python -tt
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget 
from datetime import datetime 

from django.contrib.auth.models import User
#import Image

#from PIL import Image as Img

from io import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from django.core.validators import MaxValueValidator


#from sorl.thumbnail import ImageField
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail
from django.core.files.base import ContentFile
from django_resized import ResizedImageField


from PIL import Image
from io import BytesIO

import sys

TIPO_PRENDA = (
	        ('confeccion ', 'confeccion'),	        
	        ('serigrafia', 'serigrafia'),
			('Sublimacion', 'Sublimacion'),
			('uniforme escolar', 'uniforme escolar'),
			('uniforme deportivo', 'uniforme deportivo'),
			('uniforme de trabajo', 'uniforme de trabajo'),
			('sueter', 'sueter'),
			('chumpa', 'chumpa'),
			('camisa', 'camisa'), 
			('pans', 'pans'), 
			('otros', 'otros'),
			)

TIPOTELA = (
			('Q1', 'Q1'),
			('Q2', 'Q2'),
			('KIANITA', 'KIANITA'),
			('SUPER_KIANA', 'SUPER_KIANA'),
			('ALGODON_SENCILLO', 'ALGODON_SENCILLO'),
			('ALGODON_DOBLE', 'ALGODON_DOBLE'),
			('ADIDAS', 'ADIDAS'),
			('PIQUE_POLO', 'PIQUE_POLO'),
			('SIMPLE_PIQUE', 'SIMPLE_PIQUE'),

			('EYELET', 'EYELET'),
			('SINCATEX', 'SINCATEX'),
			('LINO STRECH', 'LINO STRECH'),
			('IMPREMEABLE', 'IMPREMEABLE'),
			('SATIN', 'SATIN'),
			('LINO_OXFORD', 'LINO_OXFORD'),
			('OTRA_TELA', 'OTRA_TELA'),

			)
ESTADO2 = (
			('ENCARGADO', 'ENCARGADO'),
			('PRODUCCION', 'PRODUCCION'),
			('EMPACADO', 'EMPACADO'),
			('ENTREGADO', 'ENTREGADO'),	
			)


#class Categoria_global(models.Model):
#		 categoria=models.CharField(max_length=60,blank=True,null=True)
#		 def __str__(self):
#		 	return  self.categoria
#		 class Admin:
#		 	list_display = ('categoria')

class Categoria(models.Model):
         id_usuario=models.CharField(max_length=30,blank=True)
         tienda=models.CharField(max_length=30,blank=True,null=True)
         categoria=models.CharField(max_length=30,blank=True,null=True)
         descripcion = models.TextField(blank=True)
         
         def __str__(self):
         	return  self.categoria
         class Admin:
         	list_display = ('categoria')


ESTADO_PRODUCTO= (
	        ('EN_EXISTENCIA', 'EN_EXISTENCIA'), 
			('EN_PRODUCCION', 'EN_PRODUCCION'),
			('SOLO_POR_ENCARGO', 'SOLO_POR_ENCARGO'),
			('AGOTADO', 'AGOTADO'),	
			('VENDIDO', 'VENDIDO'),	
			
			)

PLAN_PUBLICIDAD= (
	        ('PUBLICIDAD_0','SIN_PLAN_PUBLICITARIO $0.0'), 
			('PUBLICIDAD_1','PLAN_SIEMPRE_PRIMERO $15.0/mes'),
			('PUBLICIDAD_2','PLAN_SIEMPRE_PRIMERO_DIRIGIDO $10.0/mes'),
			)
class Productos(models.Model):
	     id_usuario=models.CharField(max_length=30,blank=True)
	     tienda=models.ForeignKey('Tiendas',blank=True,null=True)
	     categoria=models.ForeignKey('Categoria',blank=True,null=True)
	     cantidad         =  models.DecimalField(max_digits=15,decimal_places=0,default=0,blank=True,null= True)
	     nombre           =  models.CharField(max_length=30)
	     codigo=models.CharField(max_length=30,blank=True)
	     #imagen1      = models.ImageField(upload_to='tmp')	  
	     imagen1 = ImageField(upload_to='tmp',blank=True)
	     imagen2 = ImageField(upload_to='tmp',blank=True)
	     imagen3 = ImageField(upload_to='tmp',blank=True)
 
	     descripcion = models.TextField(blank=True)

	     video_insercion=models.CharField(max_length=400,blank=True)
	     
	     nombre_recurso=models.CharField(max_length=40,blank=True)
	     recurso=models.URLField(blank=True)
	     nombre_recurso_de_pago=models.CharField(max_length=400,blank=True)
	     recurso_de_pago=models.CharField(max_length=400,blank=True)
	     password_de_recurso=models.CharField(max_length=4,blank=True)	      
	     nota_de_evaluacion=models.IntegerField(blank=True,default=10)
	     #estado=  models.CharField(max_length=30,choices=ESTADO) 
	     precio_de_antes= models.FloatField(default=0,blank=True,null=True)
	     precio_A  = models.FloatField(default=0,blank=True,null=True)
	     precio_B=models.FloatField(blank=True,null=True)
	     estado_prod=models.CharField(max_length=30,blank=True,choices=ESTADO_PRODUCTO,default="EN_EXISTENCIA")
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)
	     ultima_fecha_edicion = models.DateField(default=datetime.now,editable = False)
	     plan_publicidad=models.CharField(max_length=30,choices=PLAN_PUBLICIDAD,blank=True,default="PUBLICIDAD_0")	 
	     plan_publicidad_activo=models.CharField(max_length=30,choices=PLAN_PUBLICIDAD,blank=True,default="PUBLICIDAD_0")
	     fecha_inicio_plan = models.DateField(default=datetime.now)
	     fecha_final_plan = models.DateField(default=datetime.now)

	     def __str__(self):
		    		return  self.nombre
	     class Admin:
		    		list_display = ('categoria', 'cantidad', 'nombre','precio_A')
		    		

class Buscar(models.Model):
	     id_usuario=models.CharField(max_length=30,blank=True)
	     item_de_busqueda=models.CharField(max_length=30)
	     fecha_busqueda = models.DateField(default=datetime.now,editable = False)

	     def __str__(self):
		    		return  self.item_de_busqueda
	     class Admin:
		    		list_display = ('item_de_busqueda','fecha_busqueda')


PLAN_TIENDA= (
	        ('GRATIS', 'GRATIS (X PRODUCTOS MAXIMO, NO PUBLICIDAD)'), 
			('BASICO', 'BASICO (20 productos S30 ANUALES)'),
			('STANDARD', 'STANDARD (45 productos $50 ANUALES)'),
			('PREMIUM', 'PREMIUN (100 productos $90 ANUALES)'),	
			('TRECIENTOS', 'TRECIENTOS PRODUCTOS $?'),	
			('QUINIENTOS', 'QUINIENTOS PRODUCTOS $?'),	
			('MIL', 'MIL PRODUCTOS $?'),
			('DOSMIL', 'DOSMIL PRODUCTOS $?'),	
			('CINCOMIL', 'CINCOMIL PRODUCTOS $?'),		 
			       
			)	

CLAVES=(
			('NORMAL', 'NORMAL'),
			('PEDIDOS', 'PEDIDOS'),
			('ENLACES', 'ENLACES'),

						
			)

class Configuracion_sistema(models.Model):
	     mensaje_bienvenida=models.TextField(blank=True)	
	     n_visitas=models.IntegerField(blank=True,default=0) 
	               
	     def __str__(self):
		    		return  self.mensaje_bienvenida
	     class Admin:
		    		list_display = ('mensaje_bienvenida')


BANCO=(
			('BANCO_AGRICOLA', 'BANCO_AGRICOLA'),
			('BANCO_AGRICOLA', 'BANCO_AGRICOLA'),
			('BANCO_AGRICOLA', 'BANCO_AGRICOLA'),

						
			)


TIPO_USUARIO=(
			('EL_COMPRADOR', 'EL_COMPRADOR'),			
			('EL_ADMINISTRADOR', 'EL_ADMINISTRADOR'),			
			('EL_DELIBERY', 'EL_DELIBERY'),

						
			)

CIUDADES= (
	        ("AHUACHAPAN", "AHUACHAPAN"), 
	        ("SANTA_ANA","SANTA_ANA"), 
	        ("SONSONATE","SONSONATE"),
	        ("CHALATENANGO","CHALATENANGO"),
	        ( "CABAÑAS", "CABAÑAS"),
	        ("LA_LIBERTAD","LA_LIBERTAD"),
	        ("LA_PAZ","LA_PAZ"),
	        ("MORAZAN","MORAZAN"),
	        ("CUSCATLAN","CUSCATLAN"),
	        ("SAN_MIGUEL","SAN_MIGUEL"),
	        ("LA_UNION","LA_UNION"),
	        ("USULUTAN","USULUTAN"),
	        ("SAN_VICENTE","SAN_VICENTE"),
	        ("SAN_SALVADOR","SAN_SALVADOR"),							
		)
class Usuarios(models.Model):
	     id_usuario=models.CharField(max_length=30)
	     clave=models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(9999)])
	     nombre=models.CharField(max_length=40)
	     apellido=models.CharField(max_length=40)
	     image = ResizedImageField(size=[100, 100], crop=['top', 'left'], upload_to='tmp')
	     estoy_en=models.CharField(max_length=30,choices=CIUDADES)
	     comentario_opcional=models.CharField(max_length=40,blank=True,null=True)
	     nota_de_evaluacion=models.IntegerField(blank=True,default=10,null=True)
	     email = models.EmailField(blank=True,null=True)
	     plan_tienda=models.CharField(max_length=30,choices=PLAN_TIENDA,blank=True,default="GRATIS",null=True)	 
	     plan_tienda_activo=models.CharField(max_length=30,choices=PLAN_TIENDA,blank=True,default="GRATIS",null=True)
	     facedireccion=models.URLField(blank=True,null=True)
	     nombre_del_banco=models.CharField(max_length=40,blank=True,default="BANCO_AGRICOLA",null=True)
	     numero_cuenta=models.CharField(max_length=40,blank=True,null=True)
	     numero_tigo_money=models.CharField(max_length=40,blank=True,null=True)
	     codigoapk=models.CharField(max_length=30,blank=True,choices=CLAVES,default="NORMAL",null=True)
	     fecha_inicio_plan = models.DateField(default=datetime.now)
	     fecha_final_plan = models.DateField(default=datetime.now)
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)
	     tipo_de_vista=models.CharField(max_length=30,blank=True,default="NORMAL",null=True)
	     tipo_usuario=models.CharField(max_length=30,choices=TIPO_USUARIO,blank=True,default="EL_COMPRADOR",null=True)
	     tipo_vista=models.IntegerField(blank=True,default=0,null=True)
	     #def save(self):
	     ##Opening the uploaded image
	     	#im = Image.open(self.image)
	     	#output = BytesIO()
	     	##Resize/modify the image
	     	#im=im.resize( (100,100) )
	     	##after modifications, save it to the output
	     	#im.save(output, format='JPEG', quality=100)
	     	#output.seek(0)
	     	##change the imagefield value to be the newley modifed image value
	     	#self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
	     	#super(Usuarios,self).save()
	     def __str__(self):
	     		return  self.id_usuario
	     class Admin:
	     		list_display = ('id_usuario')


 
  
	    		 


   
		 


CATEGORIA_TIENDA= (
	        ('GRATIS', 'GRATIS (5 PRODUCTOS MAXIMO, NO PUBLICIDAD)'), 
			('BASICO', 'BASICO (20 productos S30 ANUALES)'),
			('STANDARD', 'STANDARD (50 productos $75 ANUALES)'),
			('PREMIUM', 'PREMIUN (100 productos $125 ANUALES)'),	
			

			)



ESTADO_TIENDA= (
	        ('DISPONIBLE', 'DISPONIBLE'), 
			('NO_DISPONIBLE', 'NO_DISPONIBLE'),						
			)




SUPER_CATEGORIA=(
("Productos Ventas Varias","Productos Ventas Varias"),
("Alimentos Bebidas","Alimentos Bebidas"),
("Antiguedades Artesanias Adornos","Antiguedades Artesanias Adornos"),
("Mascotas Acsesorios Veterinarios","Mascotas Acsesorios Veterinarios"),
("Bienes raices Alquileres Ventas","Bienes raices Alquileres Ventas"),
("Tecnologia Informatica Informacion","Tecnologia Informatica Informacion"),
("Educacion Ciencia Academias","Educacion Ciencia Academias"),
("Deportes Ocio Acsesorios","Deportes Ocio Acsesorios"),
("Herramientas Maquinaria Equipo","Herramientas Maquinaria Equipo"),
("Agro Ferreteria Maderas","Agro Ferreteria Maderas"),
("Materias primas varias","Materias primas varias"),
("Mateiales de construccion","Mateiales de construccion"),
("Muebles Electrodomesticos","Muebles Electrodomesticos"),
("Productos para el hogar","Productos para el hogar"),
("Productos de consumo diario","Productos de consumo diario"),
("Productos para la industria","Productos para la industria"),
("Industria Acsesorios Repuestos","Industria Acsesorios Repuestos"),
("Ropa Moda calzado","Ropa Moda calzado"),
("Salud Belleza","Salud Belleza"),
("Usados de todos","Usados de todos"),
("Vehiculos acsesorios repuestos","Vehiculos acsesorios repuestos"),
("Productos y Sevicios varios","Productos y Sevicios varios"),
("Servicios domesticos","Servicios domesticos"),
("Servicios personales","Servicios personales"),
("Servicios pofesionales","Servicios pofesionales"),
("Servicios de Ensenanza","Servicios de Ensenanza"),
("Sevicios financieros","Sevicios financieros"),
("Servicios publicitarios","Servicios publicitarios"),
("Servicio de reparaciones","Servicio de reparaciones"),
("Servicio de hotel alojamiento","Servicio de hotel alojamiento"),
("Otros Servicios","Otros Servicios"),

 )
 




class Ccomercial(models.Model):	     
	     id_usuario=models.CharField(max_length=30)	     
	     nombre_ccomercial=models.CharField(max_length=40,blank=True)
	     imagen_ccomercial = ImageField(upload_to='tmp',blank=True)
	     ubicacion=models.CharField(max_length=30,blank=True,choices=CIUDADES)
	     descripcion_ccomercial=models.TextField(blank=True)
	     plan_publicidad=models.CharField(max_length=30,choices=PLAN_PUBLICIDAD,blank=True,default="PUBLICIDAD_0")	 
	     plan_publicidad_activo=models.CharField(max_length=30,choices=PLAN_PUBLICIDAD,blank=True,default="PUBLICIDAD_0")
	     fecha_inicio_plan = models.DateField(default=datetime.now)
	     fecha_final_plan = models.DateField(default=datetime.now)	     
	         

	     def __str__(self):
		    		return  self.nombre_ccomercial
	     class Admin:
		    		list_display = ('nombre_ccomercial')                                                 
  
class Tiendas(models.Model):	     
	     id_usuario=models.CharField(max_length=30)	  
	     ccomercial=models.ForeignKey('Ccomercial',blank=True,null=True)   
	     nombre_tienda=models.CharField(max_length=30)
	     ubicacion=models.CharField(max_length=30,blank=True,choices=CIUDADES)
	     #categoria=models.ForeignKey('Categoria_global',blank=True,null=True)
	     categoria=models.CharField(max_length=40,blank=True,choices=SUPER_CATEGORIA)	     
	     imagen1 = ImageField(upload_to='tmp',blank=True)
	     descripcion=models.TextField(blank=True)
	     codigoapk=models.CharField(max_length=30,blank=True,choices=CLAVES,default="NORMAL")
	     tipo_de_vista=models.CharField(max_length=30,blank=True,default="NORMAL")
	     slogan=models.CharField(max_length=90,blank=True)
	     promocion=models.CharField(max_length=90,blank=True)
	     n_visitas=models.IntegerField(blank=True,default=0)
	     ultimo_comentario=models.CharField(max_length=90,blank=True)
	     nota_de_evaluacion=models.IntegerField(blank=True,default=10)
	     administrador_junior=models.CharField(max_length=30,blank=True)
	     administrador_junior_1=models.CharField(max_length=30,blank=True)
	     administrador_junior_2=models.CharField(max_length=30,blank=True)

	     plan_publicidad=models.CharField(max_length=30,choices=PLAN_PUBLICIDAD,blank=True,default="PUBLICIDAD_0")	 
	     plan_publicidad_activo=models.CharField(max_length=30,choices=PLAN_PUBLICIDAD,blank=True,default="PUBLICIDAD_0")
	     fecha_inicio_plan = models.DateField(default=datetime.now)
	     fecha_final_plan = models.DateField(default=datetime.now)	 
	    
	     estado_tienda=models.CharField(max_length=30,blank=True,choices=ESTADO_TIENDA,default="DISPONIBLE")
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)
	     ultima_fecha_edicion = models.DateField(default=datetime.now,editable = False)

	     def __str__(self):
		    		return  self.nombre_tienda
	     class Admin:
		    		list_display = ('nombre_tienda')


ESTADO_MENSAJE= (
	        ('ATENDIDO', 'ATENDIDO'), 
			('NUEVO', 'NUEVO'),
			)

class Mensajes(models.Model):
	producto=models.ForeignKey('Productos',blank=True,null=True)
	contacto=models.CharField(max_length=30,null=True)
	pregunta = models.TextField(blank=True,null=True)
	respuesta = models.TextField(blank=True,null=True)
	estado_mensaje=models.CharField(max_length=30,choices=ESTADO_MENSAJE,default="NUEVO")
	fecha= models.DateField(default=datetime.now,blank=True,editable = False)
	def __str__(self):
				return  self.pregunta
	class Admin:
				list_display = ('contacto', 'id_usuario','pregunta')





class Pedidos(models.Model):
	     id_usuario=models.CharField(max_length=30,blank=True)
	     codigo=models.CharField(max_length=30,blank=True)
	     tienda=models.ForeignKey('Tiendas',blank=True,null=True)	     
	     tipo_prenda=  models.CharField(max_length=30,choices=TIPO_PRENDA )
	     
	     nombre           =  models.CharField(max_length=30)
	     contacto=  models.CharField(max_length=30)

	     descripcion = models.TextField(blank=True)
	     #imagen1      = models.ImageField(upload_to='tmp')	  
	     imagen1 = ImageField(upload_to='tmp',blank=True)
	     imagen2 = ImageField(upload_to='tmp',blank=True)
	     imagen3 = ImageField(upload_to='tmp',blank=True)

	     precios_unitarios = models.TextField(max_length=300,blank=True)
	     total  = models.FloatField(blank=True,null=True)
	     anticipo  = models.FloatField(blank=True,null=True)
            
	     estado=  models.CharField(max_length=30,choices=ESTADO2)
	     fecha_de_entrega = models.DateField(default=datetime.now) 
	    	     
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)
     
	     cant_tela_1=models.FloatField(blank=True,null= True)
	     tipo_tela_1=models.CharField(blank=True,max_length=30,choices=TIPOTELA)
	     color_tela_1=models.CharField(blank=True,max_length=30)
	     
	     cant_tela_2=models.FloatField(blank=True,null= True)
	     tipo_tela_2=models.CharField(blank=True,max_length=30,choices=TIPOTELA)
	     color_tela_2=models.CharField(blank=True,max_length=30)
	     
	     cant_tela_3=models.FloatField(blank=True,null= True)
	     tipo_tela_3=models.CharField(blank=True,max_length=30,choices=TIPOTELA)
	     color_tela_3=models.CharField(blank=True,max_length=30)
	    

	     def __str__(self):
		    		return  self.nombre
	     class Admin:
		    		list_display = ('categoria', 'nombre','total')




from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
#from django.contrib.contenttypes import generic

class Cart(models.Model):
				creation_date = models.DateTimeField(verbose_name=_('creation date'))
				checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))

				class Meta:
								verbose_name = _('cart')
								verbose_name_plural = _('carts')
								ordering = ('-creation_date',)

				def __unicode__(self):
								return unicode(self.creation_date)

class ItemManager(models.Manager):
				def get(self, *args, **kwargs):
								if 'product' in kwargs:
												kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
												kwargs['object_id'] = kwargs['product'].pk
												del(kwargs['product'])
								return super(ItemManager, self).get(*args, **kwargs)

class Item(models.Model):
				cart = models.ForeignKey(Cart, verbose_name=_('cart'))
				quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
				unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))
				# product as generic relation
				content_type = models.ForeignKey(ContentType)
				object_id = models.PositiveIntegerField()

				objects = ItemManager()

				class Meta:
								verbose_name = _('item')
								verbose_name_plural = _('items')
								ordering = ('cart',)

				def __unicode__(self):
								return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)

				def total_price(self):
								return self.quantity * self.unit_price
				total_price = property(total_price)

				# product
				def get_product(self):
								return self.content_type.get_object_for_this_type(pk=self.object_id)

				def set_product(self, product):
								self.content_type = ContentType.objects.get_for_model(type(product))
								self.object_id = product.pk

				product = property(get_product, set_product)

ESTADO3 = (
			('QUIERO_PEDIR_ESTO', 'QUIERO_PEDIR_ESTO'),
			('EL_VENDEDOR_RECIBIO_EL_PEDIDO', 'EL_VENDEDOR_RECIBIO_EL_PEDIDO'),
			('EL_VENDEDOR_A_CONFIRMADO', 'EL_VENDEDOR_A_CONFIRMADO'),
			('PRODUCTO_ENTREGADO', 'PRODUCTO_ENTREGADO'),
			('PRODUCTO_RECIBIDO_YA', 'PRODUCTO_RECIBIDO_YA'),
			
			
			)

ENTREGA = (
			('QUIERO_PEDIR_ESTO ', 'QUIERO_PEDIR_ESTO'),
			('EL_VENDEDOR_RECIBIO_EL_PEDIDO', 'EL_VENDEDOR_RECIBIO_EL_PEDIDO'),
			('EL_VENDEDOR_A_CONFIRMADO', 'EL_VENDEDOR_A_CONFIRMADO'),
			('PRODUCTO_ENTREGADO', 'PRODUCTO_ENTREGADO'),
			('PRODUCTO_RECIBIDO_YA', 'PRODUCTO_RECIBIDO_YA'),
			
			
			)

SERVICIO = (
			('SI','Si, A domicilio $?'),
			('NO','LLegare por el pedido'),
			('TALVES','Escribame para acordar entrega'),
				
			
			)

class Carro_de_compras(models.Model):
	producto=models.ForeignKey('Productos',blank=True,null=True)
	id_comprador=models.CharField(max_length=30,blank=True,null=True)
	nombre_comprador=models.CharField(max_length=40,blank=True,null=True)
	apellido_comprador=models.CharField(max_length=40,blank=True,null=True)
	
	     
	#id_vendedor=models.CharField(max_length=30,blank=True,null=True)
	#id_producto=models.CharField(max_length=30,blank=True,null=True)

	#nombre_tienda=models.CharField(max_length=30,blank=True,null=True)
	cantidad=models.DecimalField(max_digits=4,decimal_places=0,default=0,blank=True,null= True)
	#nombre=  models.CharField(max_length=30,null=True)
	#precio = models.FloatField(default=0,blank=True,null=True)
	mostrar_foto=models.CharField(max_length=30,blank=True,null=True)	     
	especificacion = models.TextField(blank=True,null=True)
	total= models.FloatField(default=0,blank=True,null=True)
	estado_prod=models.CharField(max_length=30,blank=True,choices=ESTADO3,default="QUIERO_PEDIR_ESTO",null=True)
	fecha_ingreso = models.DateField(default=datetime.now)

	lugar_de_entrega=models.CharField(max_length=60,blank=True,null=True)	 
	fecha_de_entrega=models.CharField(max_length=30,blank=True,null=True)	 
	servicio_a_domicilio=models.CharField(max_length=30,blank=True,null=True,choices=SERVICIO)
	costo_servicio=models.FloatField(default=0,blank=True,null=True)	
	
	imagen1 = ImageField(upload_to='tmp',blank=True)
	imagen2 = ImageField(upload_to='tmp',blank=True)	

	nota_comprador=models.IntegerField(blank=True,default=0)
	nota_vendedor=models.IntegerField(blank=True,default=0)
	usuario_car=models.ForeignKey('Usuarios',blank=True,null=True)
	    

	def __str__(self):
		    		return  self.producto.nombre
	class Admin:
		    		list_display = ('especificacion','id_usuario')
	


class Preferidas(models.Model):	
	id_comprador=models.CharField(max_length=30,blank=True,null=True)
	tienda=models.ForeignKey('Tiendas',blank=True,null=True)
	fecha_ingreso = models.DateField(default=datetime.now)  

	def __str__(self):
		    		return  self.id_comprador
	class Admin:
		    		list_display = ('id_comprador')


class Evaluacion(models.Model):
	id_evaluador=models.ForeignKey('Productos',blank=True,null=True)
	id_evaluado=models.CharField(max_length=30,null=True)
	nota = models.TextField(blank=True,null=True)
	
	def __str__(self):
				return  self.id_evaluador
	class Admin:
				list_display = ('id_evaluador', 'id_evaluado','nota')
