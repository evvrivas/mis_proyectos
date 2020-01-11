
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from mysite.datos_artetronica.models import *


#admin.site.unregister(User)
from mysite.forms import *

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = UserProfileForm
class UserProfileAdmin(admin.ModelAdmin):
        model = UserProfile
        list_display = ['nombre_usuario','tipo_usuario']
        def nombre_usuario(self,instance):
                return instance.usuario.username    
admin.site.register(UserProfile,UserProfileAdmin)
####################################################

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = CodigoForm
class CodigoAdmin(admin.ModelAdmin):
        model = Codigo
        list_display = ['nombre_usuario','codigo']
        def nombre_usuario(self,instance):
                return instance.usuario.username    
admin.site.register(Codigo,CodigoAdmin)
####################################################
        

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = EstudiosForm
class EstudiosAdmin(admin.ModelAdmin):
        model = Estudios
        list_display = ['nombre','fecha_inicio','fecha_final', 'codigo','n_muestras']

admin.site.register(Estudios,EstudiosAdmin)
####################################################

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = PreguntasForm
class PreguntasAdmin(admin.ModelAdmin):
        model = Preguntas
        list_display = ['nombre_estudio','pregunta']
        
        def nombre_estudio(self,instance):
                return instance.estudio.nombre

admin.site.register(Preguntas,PreguntasAdmin)
####################################################


