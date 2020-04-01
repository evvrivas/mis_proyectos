
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
        list_display = ['id_usuario','nombre','apellido','tipo_usuario','plan_tienda_activo','codigoapk','fecha_inicio_plan','clave','cant_click_whatsapp_acumulados','cant_click_whatsapp','costo_click_whatsapp','cant_click_telefono_acumulados','cant_click_telefono','costo_click_telefono','cant_click_pedidos_nuevos_acumulados','cant_click_pedidos_nuevos','costo_click_pedidos_nuevos','venta_acumulada','venta_actual','porcentaje_venta']
        #list_filter=(('plan_tienda_activo',admin.RelatedOnlyFieldListFilter),('tipo_usuario',admin.RelatedOnlyFieldListFilter),)
           
admin.site.register(Usuarios,UsuariosAdmin)
####################################################
   
####################################################
class RulesAdmin(admin.ModelAdmin):
    form = ProductosForm
class ProductosAdmin(admin.ModelAdmin):
        model = Productos
        list_display = ['id_usuario','tienda_nombre','cantidad', 'nombre','precio_A','precio_B','estado_prod','plan_publicidad_activo','fecha_inicio_plan','fecha_final_plan','venta_acumulada','venta_actual','porcentaje_venta']
        list_filter=(('tienda',admin.RelatedOnlyFieldListFilter),('categoria',admin.RelatedOnlyFieldListFilter),)
        def tienda_nombre(self,instance):
                return instance.tienda.nombre_tienda
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
#class RulesAdmin(admin.ModelAdmin):
#    form = Categoria_globalForm
#admin.site.register(Categoria_global)
####################################################    

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = TiendasForm
class TiendasAdmin(admin.ModelAdmin):
    model = Tiendas
    list_display = ['id_usuario', 'nombre_tienda','codigoapk','n_visitas','administrador_junior','promocion','plan_publicidad_activo','fecha_inicio_plan','fecha_final_plan','cant_click_whatsapp_acumulados','cant_click_whatsapp','costo_click_whatsapp','cant_click_telefono_acumulados','cant_click_telefono','costo_click_telefono','cant_click_pedidos_nuevos_acumulados','cant_click_pedidos_nuevos','costo_click__pedidos_nuevos','venta_acumulada','venta_actual','porcentaje_venta']
        
admin.site.register(Tiendas,TiendasAdmin)
####################################################
  
####################################################
class RulesAdmin(admin.ModelAdmin):
    form = PedidosForm
class PedidosAdmin(admin.ModelAdmin):
    model = Pedidos
    list_display = ['id_usuario','nombre_tienda','nombre','tipo_prenda', 'contacto','precios_unitarios','total','anticipo','fecha_de_entrega','estado']
    list_filter=(('tienda',admin.RelatedOnlyFieldListFilter),)

    def nombre_tienda(self,instance):
        return instance.tienda.nombre_tienda
    
admin.site.register(Pedidos,PedidosAdmin)
####################################################        
        
   
####################################################
class RulesAdmin(admin.ModelAdmin):
    form = Configuracion_sistemaForm
class Configuracion_sistemaAdmin(admin.ModelAdmin):
    model = Configuracion_sistema
    list_display = ['n_visitas','mensaje_bienvenida']   
admin.site.register(Configuracion_sistema,Configuracion_sistemaAdmin)
####################################################


      
####################################################
class RulesAdmin(admin.ModelAdmin):
    form = MensajesForm
class MensajesAdmin(admin.ModelAdmin):
    model = Mensajes
    list_display = ['item','nombre_producto','contacto','pregunta','id_usuario','respuesta','estado_mensaje','fecha']
    list_filter=(('contacto',admin.RelatedOnlyFieldListFilter),('id_usuario',admin.RelatedOnlyFieldListFilter),('estado_mensaje',admin.RelatedOnlyFieldListFilter))
    
    def nombre_producto(self,instance):
        return instance.producto.nombre
    def id_usuario(self,instance):
        return instance.producto.id_usuario
    def item(self,instance):
        return instance.producto.id
admin.site.register(Mensajes,MensajesAdmin)
####################################################
   
####################################################
class RulesAdmin(admin.ModelAdmin):
    form = CcomercialForm
class CcomercialAdmin(admin.ModelAdmin):
    model = Ccomercial
    list_display = ['nombre_ccomercial','id_usuario','plan_publicidad_activo','fecha_inicio_plan','fecha_final_plan']

admin.site.register(Ccomercial,CcomercialAdmin)
####################################################
     

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = Carro_de_comprasForm
class Carro_de_comprasAdmin(admin.ModelAdmin):
    model = Carro_de_compras
    #list_display = ['id_vendedor','nombre_tienda','id_comprador','cantidad','nombre','especificacion','precio','total','estado_prod','costo_servicio_a_domicilio','fecha_ingreso']
    #list_filter=(('id_comprador',admin.RelatedOnlyFieldListFilter),('estado_prod',admin.RelatedOnlyFieldListFilter),('costo_servicio_a_domicilio',admin.RelatedOnlyFieldListFilter))
    #def id_vendedor(self,instance):
    #    return instance.producto.id_usuario
    #def nombre_tienda(self,instance):
    #    return instance.producto.tienda.nombre_tienda
    #def nombre(self,instance):
    #    return instance.producto.nombre
    #def precio(self,instance):
    #    return instance.producto.precio_A



admin.site.register(Carro_de_compras,Carro_de_comprasAdmin)
####################################################:



####################################################
class RulesAdmin(admin.ModelAdmin):
    form = PreferidasForm
class PreferidasAdmin(admin.ModelAdmin):
    model = Preferidas
    list_display = ['id_comprador','nombre_tienda','fecha_ingreso']
    
    def nombre_tienda(self,instance):
        return instance.tienda.nombre_tienda

admin.site.register(Preferidas,PreferidasAdmin)
####################################################   

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = EvaluacionForm
class EvaluacionAdmin(admin.ModelAdmin):
    model = Evaluacion
    list_display = ['id_evaluador','id_evaluado','nota']    
   
admin.site.register(Evaluacion,EvaluacionAdmin)
####################################################   

