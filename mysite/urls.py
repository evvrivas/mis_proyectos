#from django.conf.urls import patterns, include, url
#from django.contrib import admin

#from mysite.views import Index

##########################
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url,include

from django.contrib import admin


from django.conf import settings
import mysite.settings

from django.contrib.auth.views import login, logout

from django.conf.urls.static  import static 


from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from mysite.views import *
from django.conf.urls import url
from django.views.generic import TemplateView
urlpatterns = [
    # Examples:
    # url(r'^$', 'artetronica.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^admin/',include(admin.site.urls)),
    #url(r'^$', Index.as_view(), name='index'),
    url(r'^accounts/login/$', login,{'template_name': 'login.html'}),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/profile/$', pagina_principal),

    #url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  settings.MEDIA_ROOT}),
    
    url(r'^$', pagina_principal),
    url(r'^catalogo/(\d+)$', catalogo),
    url(r'^informacion/$', informacion),
    url(r'^informacion_vendedor/([^/]+)/$', informacion_vendedor),
    url(r'^informacion_comprador/([^/]+)/$', informacion_comprador),
       
    url(r'^crear_usuario/$',crear_usuario),
    url(r'^editar_usuario/$',editar_usuario),

    url(r'^crear_tienda/$',crear_tienda),
    url(r'^editar_tienda/(\d+)/$',editar_tienda),
    
    url(r'^crear_producto/([^/]+)/([^/]+)/$',crear_producto),
    url(r'^editar_producto/([^/]+)/([^/]+)/(\d+)/$',editar_producto),
         
 
    url(r'^ver_categorias/([^/]+)/$', ver_categorias),
    url(r'^ver_categorias_tienda/([^/]+)/([^/]+)/([^/]+)/$', ver_mis_categorias),
    url(r'^busqueda/([^/]+)/$', busqueda),
    url(r'^busqueda_tienda/([^/]+)/([^/]+)/$', busqueda_tienda),
    url(r'^busqueda_desde_app/([^/]+)/$', busqueda_desde_app),
    

    url(r'^editar_pedido/([^/]+)/([^/]+)/(\d+)/$',editar_pedido),
    url(r'^hacer_pedido/([^/]+)/([^/]+)/$',hacer_pedido),
    url(r'^cambiar_estado_pedido/([^/]+)/([^/]+)/(\d+)/$',cambiar_estado_pedido),
    url(r'^listado_pedido/([^/]+)/([^/]+)/([A-Z]+)/$', listado_pedido),

   
    url(r'^carrusel/(\d+)/([^/]+)/([^/]+)/$', carrusel),
    url(r'^carrusel_pedidos/(\d+)/([^/]+)/([^/]+)/$', carrusel_pedidos),
    
    url(r'^cambiar_estado_producto/([^/]+)/([^/]+)/(\d+)/([^/]+)/$',cambiar_estado_producto),
    url(r'^cambiar_estado_tienda/([^/]+)/(\d+)/([^/]+)/$',cambiar_estado_tienda),    
    url(r'^descargar/([^/]+)/([^/]+)/(\d+)/$',descargar),
    url(r'^centro_comercial/([^/]+)/([^/]+)/$',centro_comercial),   
    
    url(r'^crear_categorias/$',crear_categorias),
    url(r'^ver_las_preferidas/$',ver_las_preferidas), 
    url(r'^mis_cuentas/$',mis_cuentas),  
    

    url(r'^agregar_producto_al_carrito/(\d+)/([^/]+)/$',agregar_producto_al_carrito),  
    url(r'^ver_el_carrito/([^/]+)/$',ver_el_carrito),  


    url(r'^ver_el_carrito_personal_y_de_tienda/([^/]+)/(\d+)/$',ver_el_carrito_personal_y_de_tienda), 
    url(r'^ver_el_carrito_de_tienda/(\d+)/$',ver_el_carrito_de_tienda), 
    url(r'^ver_el_carrito_personal/([^/]+)/$',ver_el_carrito_personal), 


    url(r'^eliminar_producto_del_carrito/(\d+)/$',eliminar_producto_del_carrito),  
    url(r'^editar_producto_del_carrito/(\d+)/$',editar_producto_del_carrito),
    url(r'^editar_estado_producto_del_carrito/(\d+)/([^/]+)/$',editar_estado_producto_del_carrito), 
    url(r'^realizar_compra_individual/(\d+)/$',realizar_compra_individual),
    url(r'^realizar_compra/$',realizar_compra),

    url(r'^enviar_mensaje/(\d+)/$', enviar_mensaje),
    url(r'^ver_mis_mensajes/([^/]+)/([^/]+)/$',ver_mis_mensajes),    
    url(r'^responder_mensaje/(\d+)/$',responder_mensaje),

    
    url(r'^cambiar_tipo_de_vista/(\d+)/$',cambiar_tipo_de_vista),
    url(r'^agregar_a_preferidas/(\d+)/$',agregar_a_preferidas),
    
    url(r'^configurar_vista_pagina_principal/$',configurar_vista_pagina_principal),
    
    url(r'^evaluar/(\d+)/([^/]+)/$',evaluar), 
     
    url(r'^administrar_mis_categorias/(\d+)/$',administrar_mis_categorias),
    url(r'^traspasar_tienda/(\d+)/$',traspasar_tienda),

    url(r'^editar_categoria_de_mi_tienda/(\d+)/(\d+)/$',editar_categoria_de_mi_tienda),
    url(r'^borrar_categoria_de_mi_tienda/(\d+)/(\d+)/$',borrar_categoria_de_mi_tienda),   
    
    url(r'^comunicacion_tienda/(\d+)/([^/]+)/$',comunicacion_tienda),
    url(r'^seleccion_compra/(\d+)/(\d+)/$',seleccion_compra),
    
    url(r'^notificar_a_todos_que/$',notificar_a_todos_que),

    url(r'^guardar_token/$',guardar_token, name='guardar_token'),
    url(r'^serviceworker(.*.js)$', TemplateView.as_view(template_name='serviceworker.js',  content_type='application/x-javascript')),
     
    url(r'^realizar_lista_de_compras/(\d+)/$',realizar_lista_de_compras),
    url(r'^agregar_lista_de_compra_al_carrito/(\d+)/$',agregar_lista_de_compra_al_carrito),    
    url(r'^crear_super_producto/(\d+)/$',crear_super_producto),

    url(r'^go_tipo_uber/$',go_tipo_uber),
    url(r'^go_delivery/$',go_delivery),
      

    url(r'^([^/]+)/$', mis_tiendas),
    url(r'^([^/]+)/([^/]+)/$', mi_tienda),
       
]

    
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


