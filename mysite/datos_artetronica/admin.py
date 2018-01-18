
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.


from mysite.datos_artetronica.models import *
#admin.site.unregister(User)
from mysite.forms import *

admin.site.register(Usuarios)
class RulesAdmin(admin.ModelAdmin):
    form = UsuariosForm

admin.site.register(Productos)
class RulesAdmin(admin.ModelAdmin):
    form = ProductosForm

admin.site.register(Buscar)
class RulesAdmin(admin.ModelAdmin):
    form = BuscarForm

admin.site.register(Categoria)
class RulesAdmin(admin.ModelAdmin):
    form = CategoriaForm

    
admin.site.register(Tiendas)
class RulesAdmin(admin.ModelAdmin):
    form = TiendasForm