#!/usr/bin/python -tt
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget 
from datetime import datetime 

from django.contrib.auth.models import User
#import Image

from PIL import Image as Img

from io import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile



from sorl.thumbnail import ImageField

ESTADO= (
			('Nuevo', 'Nuevo'),
			('Usado', 'Usado'),		

			)	

class Categoria(models.Model):
		 categoria=models.CharField(max_length=30,blank=True,null=True)
		 def __str__(self):
		 	return  self.categoria
		 class Admin:
		 	list_display = ('categoria')

class Productos(models.Model):
	     id_usuario=models.CharField(max_length=30,blank=True)
	     tienda=models.ForeignKey('Tiendas',blank=True,null=True)
	     categoria=models.ForeignKey('Categoria',blank=True,null=True)
	     cantidad         =  models.DecimalField(max_digits=15,decimal_places=0,default=0)
	     nombre           =  models.CharField(max_length=30)
	     
	     #imagen1      = models.ImageField(upload_to='tmp')	  
	     imagen1 = ImageField(upload_to='tmp')
	     imagen2 = ImageField(upload_to='tmp')
	     imagen3 = ImageField(upload_to='tmp')
   
	    
	     descripcion = models.TextField(max_length=100)
	     puntuacion	 = models.CharField(max_length=30,default=0) 
	     estado=  models.CharField(max_length=30,choices=ESTADO) 
	     precio_A  = models.FloatField(blank=True,null= True	)	     
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)
	    
	     def __str__(self):
		    		return  self.nombre
	     class Admin:
		    		list_display = ('categoria', 'cantidad', 'nombre','precio_A')
		    		

class Buscar(models.Model):
	     id_usuario=models.CharField(max_length=30,blank=True)
	     item_de_busqueda=models.CharField(max_length=30)

	     def __str__(self):
		    		return  self.item_de_busqueda
	     class Admin:
		    		list_display = ('item_de_busqueda')




PLAN_TIENDA= (
	        ('GRATIS', 'GRATIS (5 PRODUCTOS MAXIMO, NO PUBLICIDAD)'), 
			('BASICO', 'BASICO (20 productos S30 ANUALES)'),
			('STANDARD', 'STANDARD (45 productos $50 ANUALES)'),
			('PREMIUM', 'PREMIUN (100 productos $90 ANUALES)'),	
			

			)	

INFORMA= (
			('informacion1', 'Acepto pagos contra entrega'),
			('informacion2', 'Acepto solamente pago anticipado'),
			('informacion3', 'Definamos el pago y la entrega'),	
			
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
            ('POLIESTER', 'POLIESTER'), 
			('EYELET', 'EYELET'),
			('SINCATEX', 'SINCATEX'),
			('LINO_STRECH', 'LINO_STRECH'),
			('IMPREMEABLE', 'IMPREMEABLE'),
			('SATIN', 'SATIN'),
			('LINO_OXFORD', 'LINO_OXFORD'),
			('TAFETA', 'TAFETA'),
			('MANTA', 'MANTA'),
			('OTRA_TELA', 'OTRA_TELA'),
			)

class Usuarios(models.Model):
	     id_usuario=models.CharField(max_length=30)
	     clave=models.CharField(max_length=4)
	     nombre=models.CharField(max_length=30,blank=True)
	     email = models.EmailField(blank=True)
	     plan_tienda=models.CharField(max_length=30,choices=PLAN_TIENDA,blank=True)	     
	     pais=models.CharField(max_length=30,blank=True)
	     direccion=models.CharField(max_length=30,blank=True)
	     codigoapk=models.CharField(max_length=30,blank=True)	     	     
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)	    
	     
	     def __str__(self):
		    		return  self.id_usuario
	     class Admin:
		    		list_display = ('id_usuario')

class Tiendas(models.Model):	     
	     id_usuario=models.CharField(max_length=30)     
	     ubicacion=models.CharField(max_length=30,blank=True)
	     nombre_tienda=models.CharField(max_length=30,blank=True)	     
	     imagen1 = ImageField(upload_to='tmp',blank=True)

	     descripcion=models.CharField(max_length=60,blank=True)
	     categoria=models.ForeignKey('Categoria',blank=True,null=True)
	     info=models.CharField(max_length=30,choices=INFORMA,blank=True)

	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)
	     	     
	     def __str__(self):
		    		return  self.nombre_tienda
	     class Admin:
		    		list_display = ('nombre_tienda')


class Pedidos(models.Model):	     
	     id_usuario=models.CharField(max_length=30)     
	     nombre=models.CharField(max_length=30)
	     contacto=models.CharField(max_length=30)	     
	     imagen1 = ImageField(upload_to='tmp',blank=True)  
	     imagen2 = ImageField(upload_to='tmp',blank=True) 
	     imagen3 = ImageField(upload_to='tmp',blank=True)
	     descripcion=models.CharField(max_length=30,blank=True)
	     categoria=models.ForeignKey('Categoria',blank=True,null=True)
	     total  = models.FloatField()
	     anticipo  = models.FloatField()
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
		    		return  self.id_usuario
	     class Admin:
		    		list_display = ('id_usuario')

class Mensajes(models.Model):
		id_usuario=models.IntegerField(blank=True,default=0)
		mensaje = models.TextField() 
		respuesta = models.TextField(blank=True)
		fecha= models.DateField(default=datetime.now,blank=True,editable = False)
		def __str__(self):
				return  self.mensaje
		class Admin:
				pass