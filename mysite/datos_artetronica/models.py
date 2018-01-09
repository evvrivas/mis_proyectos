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

 

CATEGORIA = (
			('ver todos', 'ver todos'),
              
			)



PUNTUACION = (
			('1 de 10', '1 de 10'),
			('2 de 10', '2 de 10'),
			('3 de 10', '3 de 10'),
			('4 de 10', '4 de 10'),
			('5 de 10', '5 de 10'),
			('6 de 10', '6 de 10'),
			('7 de 10', '7 de 10'),
			('8 de 10', '8 de 10'),
			('9 de 10', '9 de 10'),
			('10 de 10', '10 de 10'),

			)

	
ESTADO= (
			('Ya lo vendi', 'Ya lo vendi'),
			('Disponible', 'Disponible'),		

			)	

class Categoria(models.Model):
		 categoria=models.CharField(max_length=30)
		 def __str__(self):
		 	return  self.categoria
		 class Admin:
		 	list_display = ('categoria')

class Productos(models.Model):
	     id_usuario=models.CharField(max_length=30,blank=True)
	     categoria=models.ForeignKey('Categoria')
	     cantidad         =  models.DecimalField(max_digits=15,decimal_places=0,default=0)
	     nombre           =  models.CharField(max_length=30)
	     
	     #imagen1      = models.ImageField(upload_to='tmp')	  
	     imagen1 = ImageField(upload_to='tmp')
   
	    
	     descripcion = models.TextField(max_length=100)
	     puntuacion	 = models.CharField(max_length=30,choices=PUNTUACION) 
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
			('BASICO', 'BASICO'),
			('BASICO_CON_PUBLICIDAD', 'BASICO_CON_PUBLICIDAD'),
			('PREMIUN', 'PREMIUN'),	
			('PREMIUN_CON_PUBLICIDAD', 'PREMIUN_CON_PUBLICIDAD'),		

			)	

class Usuarios(models.Model):
	     id_usuario=models.CharField(max_length=30)
	     clave=models.CharField(max_length=4)
	     plan_tienda=models.CharField(max_length=30,choices=PLAN_TIENDA,blank=True)
	     email = models.EmailField(blank=True)
	     ubicacion=models.CharField(max_length=30,blank=True)
	     nombre_tienda=models.CharField(max_length=30,blank=True)	     
	     #imagen1      = models.ImageField(upload_to='tmp',blank=True)
	     imagen1 = ImageField(upload_to='tmp',blank=True)
	     slogan=models.CharField(max_length=30,blank=True)
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


