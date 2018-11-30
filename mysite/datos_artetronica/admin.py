
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.


from mysite.datos_artetronica.models import *
from mysite.datos_artetronica.models_cel import *

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

admin.site.register(Categoria_global)
class RulesAdmin(admin.ModelAdmin):
    form = Categoria_globalForm
    
admin.site.register(Tiendas)
class RulesAdmin(admin.ModelAdmin):
    form = TiendasForm


admin.site.register(Pedidos)
class RulesAdmin(admin.ModelAdmin):
    form = PedidosForm


admin.site.register(Configuracion_sistema)
class RulesAdmin(admin.ModelAdmin):
    form = Configuracion_sistemaForm

admin.site.register(Mensajes)
class RulesAdmin(admin.ModelAdmin):
    form = MensajesForm

    
admin.site.register(Ccomercial)
class RulesAdmin(admin.ModelAdmin):
    form = CcomercialForm