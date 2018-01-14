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
	     categoria=models.ForeignKey('Categoria',blank=True,null=True)
	     cantidad         =  models.DecimalField(max_digits=15,decimal_places=0,default=0)
	     nombre           =  models.CharField(max_length=30)
	     
	     #imagen1      = models.ImageField(upload_to='tmp')	  
	     imagen1 = ImageField(upload_to='tmp')
   
	    
	     descripcion = models.TextField(max_length=100)
	     puntuacion	 = models.CharField(max_length=30,default=0) 
	     estado=  models.CharField(max_length=30,choices=ESTADO) 
	     precio_A  = models.FloatField(blank=True,null= True	)	     
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)
	     #def save(self, *args, **kwargs):
         #	if self.imagen1:
	      #      image = Img.open(StringIO(self.imagen1.read()))
	       #     image.thumbnail((400,400), Img.ANTIALIAS)
	        #    output = StringIO()
	         #   image.save(output, format='JPEG', quality=75)
	          #  output.seek(0)
	           # self.imagen1= InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.imagen1.name, 'image/jpeg', output.len, None)
	        #super(Productos, self).save(*args, **kwargs)

	     def __str__(self):
		    		return  self.nombre
	     class Admin:
		    		list_display = ('categoria', 'cantidad', 'nombre','precio_A')
		    		#ordering = ('fecha_ingreso')
		    		#search_fields = ('nombre')#

class Buscar(models.Model):
	     id_usuario=models.CharField(max_length=30,blank=True)
	     item_de_busqueda=models.CharField(max_length=30)

	     def __str__(self):
		    		return  self.item_de_busqueda
	     class Admin:
		    		list_display = ('item_de_busqueda')




PLAN_TIENDA= (
			('BASICO', 'BASICO S30 ANUALES'),
			('STANDARD', 'STANDARD $50 ANUALES'),
			('PREMIUM', 'PREMIUN $90 ANUALES '),	
			('ILIMITADO', 'ILIMITADO $160 ANUALES'),		

			)	

INFORMA= (
			('informacion1', 'Acepto pagos contra entrega'),
			('informacion2', 'Acepto solamente pago anticipado'),
			('informacion3', 'Definamos el pago y la entrega'),	
			
			)	

class Usuarios(models.Model):
	     id_usuario=models.CharField(max_length=30)
	     clave=models.CharField(max_length=4)
	     plan_tienda=models.CharField(max_length=30,choices=PLAN_TIENDA,blank=True)
	     email = models.EmailField(blank=True)
	     ubicacion=models.CharField(max_length=30,blank=True)
	     nombre_tienda=models.CharField(max_length=30,blank=True)	     
	     imagen1 = ImageField(upload_to='tmp',blank=True)
	     descripcion=models.CharField(max_length=30,blank=True)
	     categoria=models.ForeignKey('Categoria',blank=True,null=True)
	     info=models.CharField(max_length=30,choices=INFORMA,blank=True)

	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)

	     #def save(self, *args, **kwargs):
         #	if self.imagen1:
	      #      image = Img.open(StringIO(self.imagen1.read()))
	       #     image.thumbnail((250,200), Img.ANTIALIAS)
	        #    output = StringIO()
	         #   image.save(output, format='JPEG', quality=75)
	          #  output.seek(0)
	           # self.imagen1= InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.imagen1.name, 'image/jpeg', output.len, None)
	        #super(Usuarios, self).save(*args, **kwargs)
	     
	     def __str__(self):
		    		return  self.id_usuario
	     class Admin:
		    		list_display = ('id_usuario')


