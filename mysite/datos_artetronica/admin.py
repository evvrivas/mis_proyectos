
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
        list_display = ['nombre', 'plan_tienda_activo','codigoapk','email','fecha_inicio_plan','fecha_final_plan','clave']
       
         
admin.site.register(Usuarios,UsuariosAdmin)
####################################################
   
####################################################
class RulesAdmin(admin.ModelAdmin):
    form = ProductosForm
class ProductosAdmin(admin.ModelAdmin):
        model = Productos
        list_display = ['id_usuario','tienda_nombre','cantidad', 'nombre','precio_A','precio_B','estado_prod']
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
class RulesAdmin(admin.ModelAdmin):
    form = Categoria_globalForm
admin.site.register(Categoria_global)
####################################################    

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = TiendasForm
class TiendasAdmin(admin.ModelAdmin):
    model = Tiendas
    list_display = ['id_usuario','centro_comecial', 'nombre_tienda','codigoapk','nombre_categoria','n_visitas','administrador_junior','promocion']
    list_filter=(('ccomercial',admin.RelatedOnlyFieldListFilter),('categoria',admin.RelatedOnlyFieldListFilter),)
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
    list_display = ['id_usuario','nombre_producto','contacto','pregunta','respuesta','estado','fecha']
 
admin.site.register(Mensajes,MensajesAdmin)
####################################################
   
####################################################
class RulesAdmin(admin.ModelAdmin):
    form = CcomercialForm
class CcomercialAdmin(admin.ModelAdmin):
    model = Ccomercial
    list_display = ['nombre_ccomercial','id_usuario']

admin.site.register(Ccomercial,CcomercialAdmin)
####################################################
     
cantidad=models.DecimalField(max_digits=4,decimal_places=0,default=0,blank=True,null= True)      
         precio=models.DecimalField(max_digits=4,decimal_places=0,default=0,blank=True,null= True)
         nombre= models.CharField(max_length=30)
         especificacion = models.TextField(blank=True,null=True)         
         estado_prod=models.CharField(max_length=30,blank=True,choices=ESTADO3,default="EN_EXISTENCIA")
         fecha_ingreso = models.DateField(default=datetime.now,editable = False)

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = Carro_de_comprasForm


class Carro_de_comprasAdmin(admin.ModelAdmin):
    model = Carro_de_compras
    list_display = ['contacto_tienda','nombre_tienda','id_usuario','cantidad','nombre_producto','especificacion','precio_A','precio_B','estado_prod','fecha_ingreso']
   

    def nombre_producto(self,instance):
        return instance.producto.nombre
    def precio_A(self,instance):
        return instance.producto.precio_A 
    def precio_B(self,instance):
        return instance.producto.precio_B 
    def nombre_tienda(self,instance):
        return instance.producto.tienda.nombre_tienda 
    def contacto_tienda(self,instance):
        return instance.producto.tienda.id_usuario 

admin.site.register(Carro_de_compras,Carro_de_comprasAdmin)
####################################################

          