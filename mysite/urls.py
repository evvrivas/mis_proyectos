#from django.conf.urls import patterns, include, url
#from django.contrib import admin

#from mysite.views import Index

############################################
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









urlpatterns = [
    # Examples:
    # url(r'^$', 'artetronica.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^admin/',include(admin.site.urls)),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^accounts/login/$', login,{'template_name': 'login.html'}),
    url(r'^accounts/logout/$', logout),
    #url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  settings.MEDIA_ROOT}),
    
    url(r'^principal/$', pagina_principal),
    url(r'^catalogo/(\d+)$', catalogo),
    url(r'^informacion/$', informacion),

    url(r'^editar/(\d+)/$', editar),
    
    url(r'^crear_usuario/$',crear_usuario),
    url(r'^editar_usuario/(\d+)/$',editar_usuario),

    url(r'^crear_tienda/([^/]+)/$',crear_tienda),
    url(r'^editar_tienda/([^/]+)/(\d+)/$',editar_tienda),
    
    url(r'^crear_producto/([^/]+)/([^/]+)/$',crear_producto),
    url(r'^editar_producto/([^/]+)/([^/]+)/(\d+)/$',editar_producto),

    
    url(r'^crear_mensaje/$',crear_mensaje),
    #url(r'^editar_mensaje/(\d+)/$',editar_mensaje),
  
   
  
    url(r'^get_cart/$', get_cart),
    url(r'^ver_categorias/([^/]+)/$', ver_categorias),
    url(r'^ver_categorias_tienda/([^/]+)/([^/]+)/([^/]+)/$', ver_mis_categorias),
    url(r'^busqueda/$', busqueda),
    url(r'^busqueda_tienda/([^/]+)/([^/]+)/$', busqueda_tienda),
    url(r'^([^/]+)/$', mis_tiendas),
    url(r'^([^/]+)/([^/]+)/$', mi_tienda),

    url(r'^editar_pedido/([^/]+)/([^/]+)/(\d+)/$',editar_pedido),
    url(r'^hacer_pedido/([^/]+)/([^/]+)/$',hacer_pedido),
    url(r'^cambiar_estado_pedido/([^/]+)/([^/]+)/(\d+)/$',cambiar_estado_pedido),
    url(r'^listado_pedido/([^/]+)/([^/]+)/([A-Z]+)/$', listado_pedido)
   
]

    
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


