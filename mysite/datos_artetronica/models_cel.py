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


from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
#from django.contrib.contenttypes import generic


class Central_generadora():
	     codigo=models.CharField(max_length=60,blank=True)
	     nombre=CharField(max_length=60,blank=True)	     
	     imagen1 = ImageField(upload_to='tmp',blank=True)	    
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)
	     
	     def __str__(self):
		    		return  self.codigo
	     class Admin:
		    		list_display = ('codigo', 'nombre')


class Transformador(models.Model):

	     central=models..ForeignKey('Central_generadora')
	     codigo=models.CharField(max_length=60,blank=True)
	     marca=models.CharField(max_length=60,blank=True)
	     modelo=models.CharField(max_length=60,blank=True)
	     cararcteristicas=models.TextField(blank=True)  	     
	     #imagen1      = models.ImageField(upload_to='tmp')	  
	     imagen1 = ImageField(upload_to='tmp',blank=True)	    
	     #nombre_recurso=models.CharField(max_length=40,blank=True)
	     #recurso=models.URLField(blank=True)	     
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)	     

	     def __str__(self):
		    		return  self.codigo
	     class Admin:
		    		list_display = ('codigo', 'marca', 'modelo','caracteristicas')



from django.contrib.postgres.fields import ArrayField


class Medicion(models.Model):

	     equipo=models.ForeignKey('Transformador')	     
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)	
	     d0=models.FloatField(default=0,blank=True,null=True)
	     d1=models.FloatField(default=0,blank=True,null=True)
	     d2=models.FloatField(default=0,blank=True,null=True)
	     d3=models.FloatField(default=0,blank=True,null=True)
	     d4=models.FloatField(default=0,blank=True,null=True)
	     d5=models.FloatField(default=0,blank=True,null=True)
	     d6=models.FloatField(default=0,blank=True,null=True)
	     d7=models.FloatField(default=0,blank=True,null=True)
	     d8=models.FloatField(default=0,blank=True,null=True)
	     d9=models.FloatField(default=0,blank=True,null=True)
	     
	     def __str__(self):
		    		return  self.equipo
	     class Admin:
		    		list_display = ('equipo', 'fecha')