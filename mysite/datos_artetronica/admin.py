
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from mysite.datos_artetronica.models import *


#admin.site.unregister(User)
from mysite.forms import *

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = UsuariosForm
class UsuariosAdmin(admin.ModelAdmin):
        model = Usuarios
        list_display = ['nombre', 'email','fecha_ingreso',]
    
admin.site.register(Usuarios,UsuariosAdmin)
####################################################
   
####################################################
class RulesAdmin(admin.ModelAdmin):
    form = ProductosForm
class ProductosAdmin(admin.ModelAdmin):
        model = Productos
        list_display = ['tienda_nombre', 'nombre','precio_A','estado_prod']
        def tienda_nombre(self,instance):
                return instance.tienda.nombre
admin.site.register(Productos,ProductosAdmin)
####################################################
         
####################################################
class RulesAdmin(admin.ModelAdmin):
    form = BuscarForm
class BuscarAdmin(admin.ModelAdmin):
    model = Buscar
    list_display = ['id_usuario','item_de_busqueda', 'fecha_busqueda']  
admin.site.register(Buscar,BuscarAdmin)
####################################################

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = CategoriaForm
class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria
    list_display = ['id_usuario','tienda', 'categoria']   
admin.site.register(Categoria,CategoriaAdmin)
####################################################

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = Categoria_globalForm
admin.site.register(Categoria_global)
####################################################    

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = TiendasForm
class TiendasAdmin(admin.ModelAdmin):
    model = Tiendas
    list_display = ['id_usuario','centro_comecial', 'nombre_tienda','nombre_categoria','n_visitas','administrador_junior','promocion']
    
    def centro_comecial(self,instance):
        return instance.ccomercial.nombre_ccomercial
    def nombre_categoria(self,instance):
        return instance.categoria.categoria
admin.site.register(Tiendas,TiendasAdmin)
####################################################
  
####################################################
class RulesAdmin(admin.ModelAdmin):
    form = PedidosForm
class PedidosAdmin(admin.ModelAdmin):
    model = Pedidos
    list_display = ['nombre_tienda','nombre','tipo_prenda', 'contacto','precios_unitarios','total','anticipo','fecha_de_entrega','estado']
    
    def nombre_tienda(self,instance):
        return instance.tienda.nombre_tienda
    
admin.site.register(Pedidos,PedidosAdmin)
####################################################        
        
   
####################################################
class RulesAdmin(admin.ModelAdmin):
    form = Configuracion_sistemaForm
class Configuracion_sistemaAdmin(admin.ModelAdmin):
    model = Pedidos
    list_display = ['n_visitas','mensaje_bienvenida']   
admin.site.register(Configuracion_sistema,Configuracion_sistemaAdmin)
####################################################

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = MensajesForm
class MensajesAdmin(admin.ModelAdmin):
    model = Mensajes
    list_display = ['nombre_producto','contacto','pregunta', 'pregunta','respuesta','estado','fecha']

admin.site.register(Mensajes,MensajesAdmin)
####################################################
   
####################################################
class RulesAdmin(admin.ModelAdmin):
    form = CcomercialForm
class CcomercialAdmin(admin.ModelAdmin):
    model = Mensajes
    list_display = ['nombre_ccomercial','id_usuario']

admin.site.register(Ccomercial,CcomercialAdmin)
####################################################
 
    