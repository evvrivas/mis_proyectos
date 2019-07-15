#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic import View
from django import get_version
from django.http import HttpResponse

class Index(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Running Django ' + str(get_version()) + " on OpenShift")


from django.template.loader import get_template
from django.template import Context

from django.template import RequestContext, loader

from django.http import HttpResponse
import datetime

#from books.models import Publisher
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
#from miPagina.books.models import Book
from mysite.settings import MEDIA_URL


from django.contrib import auth
from django.core.files.uploadedfile import SimpleUploadedFile 
from django.contrib.auth.decorators import login_required



from mysite.forms import *
from mysite.datos_artetronica.models import *
from mysite.datos_artetronica.cart import *

from django.contrib.auth.models import User  
from django.core.mail import send_mail
#from templates import *
from django.db.models import Q



from django.db import connection

from random import sample
def probando():
  categorias=["Productos Ventas Varias","Alimentos bebidas","Antiguedades artesanias Adornos","Mascotas acsesorios veterinarios",
                "Bienes raices alquileres ventas","Tecnologia informatica informacion","Educacion ciencia Academias",
                "Deportes ocio acsesorios","Herramientas maquinaria equipo","Agro ferreteria maderas","Materias primas varias",
                "Mateiales de construccion","Muebles electrodomesticos","Productos para el hogar","Productos de consumo diario",
                "Productos para la industria","Industria acsesorios repuestos","Ropa Moda calzado","Salud belleza",
                "Usados de todos","Vehiculos acsesorios repuestos","Productos y Sevicios varios","Servicios domesticos",
                "Servicios personales","Servicios pofesionales","Servicios de Ensenanza","Sevicios financieros",
                "Servicios publicitarios","Servicio de reparaiones","Servicio de hotel alojamiento","Otros Servicios"]
  
  for i in categorias:
      cat=Categoria_global(categoria=i)
      cat.save()


def crear_categorias(request):
  categorias=["Productos Ventas Varias","Alimentos bebidas","Antiguedades artesanias Adornos","Mascotas acsesorios veterinarios",
                "Bienes raices alquileres ventas","Tecnologia informatica informacion","Educacion ciencia Academias",
                "Deportes ocio acsesorios","Herramientas maquinaria equipo","Agro ferreteria maderas","Materias primas varias",
                "Mateiales de construccion","Muebles electrodomesticos","Productos para el hogar","Productos de consumo diario",
                "Productos para la industria","Industria acsesorios repuestos","Ropa Moda calzado","Salud belleza",
                "Usados de todos","Vehiculos acsesorios repuestos","Productos y Sevicios varios","Servicios domesticos",
                "Servicios personales","Servicios pofesionales","Servicios de Ensenanza","Sevicios financieros",
                "Servicios publicitarios","Servicio de reparaiones","Servicio de hotel alojamiento","Otros Servicios"]
  
  for i in categorias:
      cat=Categoria_global(categoria=i)
      cat.save()


  conf=Configuracion_sistema(mensaje_bienvenida="Bienvenido a DETODONEGOCIO, Has tu compra, nosotros financiamos el 50% Inicial de la compra", n_visitas=0)
  conf.save()
  
 

  fechita=datetime.datetime.now()

  u1=User.objects.create_user(username="50378218224", password="1111",email="evvrivas@gmail.com",first_name="Ernesto",last_name="Valdez")
  u1.save()

  u1=User.objects.create_user(username="50378218223", password="1111",email="evvrivas@gmail.com",first_name="Ernesto",last_name="Valdez")
  u1.save()


  us=Usuarios(id_usuario="50378218224", clave="1111", nombre="Ernesto", email ="evvrivas@gmail.com", plan_tienda="GRATIS",plan_tienda_activo="GRATIS",pais="El Salvador",facedireccion="",codigoapk="NORMAL",fecha_inicio_plan = fechita,fecha_final_plan = fechita, fecha_ingreso = fechita)      
  us.save()

  us=Usuarios(id_usuario="50378218223", clave="1111", nombre="Ernesto", email ="evvrivas@gmail.com", plan_tienda="GRATIS",plan_tienda_activo="GRATIS",pais="El Salvador",facedireccion="",codigoapk="NORMAL",fecha_inicio_plan = fechita,fecha_final_plan = fechita, fecha_ingreso = fechita)      
  us.save()



  return render(request,'principal.html',locals())







   
def logout(request):
    auth.logout(request)
    
    return HttpResponseRedirect("/")



def info_usuario():

    usuario=Usuarios.objects.filter(id_usuario=request.user.username).firrst()
    cantidad_tiendas=Tiendas.objects.filter(id_usuario=request.user.username).count()    
    tiendas=Tiendas.objects.filter(id_usuario=request.user.username)


    cN_pedidos,vN_pedidos=conteo_pedidos()
    c_msg,v_msg=conteo_mensajes()    
    connection.close()
    return cantidad_usuarios, cantidad_tiendas, cantidad_productos,cN_pedido,vN_pedido




def info_pagina():
    cantidad_usuarios=Usuarios.objects.all().count()
    cantidad_tiendas=Tiendas.objects.all().count()
    cantidad_productos=Productos.objects.all().count()
    try:
          cantidad_pedidos=Carro_de_compras.objects.filter(id_comprador=request.user.username).count()+Carro_de_compras.objects.filter(producto__id_usuario=request.user.username).count()
          cantidad_mensajes=Mensajes.objects.filter(contacto=request.user.username).count()+Mensajes.objects.filter(producto__id_usuario=request.user.username).count()
    except:  
          cantidad_pedidos=0  
          cantidad_mensajes=0  
    connection.close()
    return cantidad_usuarios, cantidad_tiendas, cantidad_productos,cantidad_pedidos,cantidad_mensajes



@login_required
def crear_producto(request,idusuario,nombretienda):               

     #!/usr/bin/python
     # -*- coding: latin-1 -*-
     import os, sys
     categoria=categorizar(idusuario,nombretienda)
  
     tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()
     var=tiendas.codigoapk 
     cantidad_productos=Productos.objects.filter(id_usuario=request.user.username).count()
     
     usuario=Usuarios.objects.filter(id_usuario=request.user.username).first()
     
     bandera=0
     if  usuario.plan_tienda_activo=="GRATIS" and cantidad_productos<5:
            bandera=1
     elif  usuario.plan_tienda_activo=="BASICO" and cantidad_productos<20:
            bandera=1
     elif  usuario.plan_tienda_activo=="STANDARD" and cantidad_productos<50:
            bandera=1
     elif  usuario.plan_tienda_activo=="PREMIUM" and cantidad_productos<100:
            bandera=1 
     elif  usuario.plan_tienda_activo=="TRECIENTOS" and cantidad_productos<300:
            bandera=1 
     elif  usuario.plan_tienda_activo=="QUINIENTOS" and cantidad_productos<500:
            bandera=1 
     elif  usuario.plan_tienda_activo=="MIL" and cantidad_productos<1000:
            bandera=1 
     elif  usuario.plan_tienda_activo=="DOSMIL" and cantidad_productos<2000:
            bandera=1 
     elif  usuario.plan_tienda_activo=="CINCOMIL" and cantidad_productos<2000:
            bandera=1 
     else:
           bandera=0

                 
     if bandera==1:
    

                 if request.method == 'POST': # si el usuario est enviando el formulario con datos
                        
                              form=ProductosForm(request.user.username,tiendas.nombre_tienda,request.POST,request.FILES)                   
                              
                              if form.is_valid():
                                      productillo = form.save(commit=False)
                                      # commit=False tells Django that "Don't send this to database yet.
                                      # I have more things I want to do with it."
                                      productillo.id_usuario = request.user.username # Set the user object here             
                                      productillo.tienda=tiendas             
                                      productillo.save() # Now you can send it to DB
                                      form.save()  
                                      
                                      #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                                      connection.close()
                                      return render(request,'confirmar_tienda.html',locals())     
                              else:


                                      formCateg=CategoriaForm(request.POST,request.FILES) 
                                      if formCateg.is_valid() :                           

                                              categor = formCateg.save(commit=False)
                                              # commit=False tells Django that "Don't send this to database yet.
                                              # I have more things I want to do with it."
                                              categor.id_usuario = request.user.username # Set the user object here
                                              categor.tienda = tiendas.nombre_tienda
                                              categor.save() # Now you can send it to DB
                                              formCateg.save() # Guardar los datos en la base de datos  print  
                                              connection.close() 
                                              return render(request,'entrada_producto.html',locals())                           
                                             
                                                      
                 else:
                    
                    form=ProductosForm(request.user.username,tiendas.nombre_tienda)
                    formCateg=CategoriaForm() 
                    connection.close()                      
                    return render(request,'entrada_producto.html',locals())


     else:

          connection.close()
          return render(request,'formulario_cambio_plan.html',locals())

def categorizar(idusuario,nombretienda):
        from collections import Counter
        vector=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__contains=nombretienda))
        cat=[]
        for i in vector:
              cat.append(i.categoria)              
        categoria=set(cat) 
        connection.close()       
        return categoria


def publicida_inteligencia(request):
    
    items=Buscar.objects.filter(id_usuario=request.user.username).order_by("-fecha_busqueda").first()
    palabra=items.item_de_busqueda
            
    productos= Productos.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra)).order_by("id")[:6]
    tiendas= Tiendas.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre_tienda__icontains=palabra) | Q(descripcion__icontains=palabra)).order_by("id")[:6]
    comercio= Ccomercial.objects.filter(Q(nombre_ccomercial__icontains=palabra) | Q(ubicacion__icontains=palabra) | Q(descripcion_ccomercial__icontains=palabra)).order_by("id")[:3] 
             
    connection.close()       
    return  comercio,tiendas,productos


def editar_producto(request,idusuario,nombretienda,acid):   
        categoria=categorizar(idusuario,nombretienda)
  
        tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()
        var=tiendas.codigoapk 
        
        f = Productos.objects.get(pk=acid)           
       
        if request.method == 'POST':
            
            form = ProductosForm(request.user.username,tiendas.nombre_tienda,request.POST,request.FILES,instance=f)
       
            if form.is_valid():
                    productillo = form.save(commit=False)
                    # commit=False tells Django that "Don't send this to database yet.
                    # I have more things I want to do with it."
                    productillo.id_usuario = request.user.username # Set the user object here             
                    productillo.tienda=tiendas 
                    productillo.ultima_fecha_edicion=datetime.datetime.now()             
                    productillo.save() # Now you can send it to DB
                    form.save()
                    connection.close() 
                    productos=[]
                    productos.append(f)

                    return render(request,'catalogo_tienda.html',locals())      

                                          
            
            else:

                          formCateg=CategoriaForm(request.POST,request.FILES) 
                          if formCateg.is_valid() :                           

                                  categor = formCateg.save(commit=False)
                                  # commit=False tells Django that "Don't send this to database yet.
                                  # I have more things I want to do with it."
                                  categor.id_usuario = request.user.username # Set the user object here
                                  categor.save() # Now you can send it to DB
                                  formCateg.save() # Guardar los datos en la base de datos  print  
                                  connection.close()
                                  return render(request,'entrada_producto.html',locals())  
        else:
            
            form = ProductosForm(request.user.username,tiendas.nombre_tienda,instance=f)
            #formCateg=CategoriaForm()

        
        connection.close()
        #return render_to_response('formulario.html', locals(),context_instance=RequestContext(request))
        return render(request,'entrada_producto.html',locals())   
        


def n_categorias():
         from collections import Counter         
         #cat=Categoria_global.objects.all().order_by("categoria")
         cat=Tiendas.objects.all()
         v=[]
         for i in cat:
             v.append(i.categoria)

         categoria=dict(Counter(v))
         connection.close()
         return categoria
          

def crear_usuario(request): 
        #!/usr/bin/python
        # -*- coding: latin-1 -*-
        categoria=n_categorias()
        
        n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
        mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)

        import os, sys
       
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
               
              
                    form = UsuariosForm(request.POST,request.FILES)                      
                    
                    if form.is_valid() :                        
                            
                            whatsapp = form.cleaned_data['id_usuario']
                            contra = form.cleaned_data['clave'] 
                                            
                            user = User.objects.create_user(username=whatsapp, password=contra)
                                                       
                            usuario = form.save(commit=False)
                            # commit=False tells Django that "Don't send this to database yet.
                            # I have more things I want to do with it."
                            usuario.id_usuario = user.username # Set the user object here
                            usuario.save() # Now you can send it to DB
                            form.save() # Guardar los datos en la base de datos  print 
                            user.save()  
                            
                            fecha= datetime.datetime.now()
                            mensaje= str(fecha)+"  "+str(whatsapp) + "Acaba de registrarse "+"\n"
                            sender =str("xgangasx@gmail.com")
                            asunto="nuevo usuario"+" "+ str(whatsapp)
                            try:
                                 send_mail(asunto, mensaje,"xgangasx@gmail.com",(sender,), fail_silently=False)            
                            except:
                                  pass
                            #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                            connection.close()
                            return render(request,'confirmar_usuario.html',locals())                  
                

        else:            
                         
                         form=UsuariosForm()
        connection.close()                  
        return render(request,'formulario_crear_usuario.html',locals()) 

        

def editar_usuario(request,acid):   
       categoria=n_categorias()
       n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
       mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
       a=eval(acid)-1

       acido=str(a)
       f = Usuarios.objects.get(pk=acido)           
       
       if request.method == 'POST':
            
            form = UsuariosForm(request.POST,request.FILES,instance=f)
       
            if form.is_valid():

                    contra = form.cleaned_data['clave'] 

                    user = User.objects.get(username=request.user.username)
                    user.set_password(contra)
                    user.save()

                    usu=form.save(commit=False)
                    usu.id_usuario = request.user.username
                    usu.save() # Guardar los datos en la base de datos 
                    #return render_to_response('confirmar.html',locals(),context_instance=RequestContext(request))
                    
                    whatsapp=request.user.username
                    fecha= datetime.datetime.now()
                    mensaje= str(fecha)+"  "+str(whatsapp) + "EDITO SU ESTADO "+"\n"
                    sender =str("xgangasx@gmail.com")
                    asunto="edita"+" "+ str(whatsapp)
                    try:
                        send_mail(asunto, mensaje,"xgangasx@gmail.com",(sender,), fail_silently=False) 
                    except:
                         pass        
                    connection.close()
                    return render(request,'confirmar.html',locals())             
            
       else:
            
            form = UsuariosForm(instance=f)
            

        

       connection.close()
       #return render_to_response('formulario.html', locals(),context_instance=RequestContext(request))
       return render(request,'formulario_editar_usuario.html',locals())   

@login_required
def crear_tienda(request):                

     #!/usr/bin/python
     # -*- coding: latin-1 -*-
     import os, sys
     categoria=n_categorias()
     n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
     mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username) 
    
     if request.method == 'POST': # si el usuario est enviando el formulario con datos
            form=TiendasForm(request.user.username,request.POST,request.FILES)                   
                  
            if form.is_valid():
                          tiendecilla = form.save(commit=False)
                          # commit=False tells Django that "Don't send this to database yet.
                          # I have more things I want to do with it."
                          tiendecilla.id_usuario = request.user.username # Set the user object here             
                                           
                          tiendecilla.save() # Now you can send it to DB
                          form.save()  
                          connection.close()
                          #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                          
                          return render(request,'confirmar.html',locals())     
            else:


                                      formCcomercial=CcomercialForm(request.POST,request.FILES) 
                                      if formCcomercial.is_valid() :                           

                                              Ccomer = formCcomercial.save(commit=False)
                                              # commit=False tells Django that "Don't send this to database yet.
                                              # I have more things I want to do with it."
                                              Ccomer.id_usuario = request.user.username # Set the user object here
                                              
                                              Ccomer.save() # Now you can send it to DB
                                              formCcomercial.save() # Guardar los datos en la base de datos  print  
                                              connection.close() 
                                              return render(request,'formulario_ingreso.html',locals())                           
                                                                           
                                 
                                          
     else:
        formCcomercial=CcomercialForm()
        form=TiendasForm(request.user.username)


                                

     connection.close() 
     return render(request,'formulario_ingreso.html',locals())
        #return render_to_response('formulario.html', locals() ,context_instance=RequestContext(request))

def editar_tienda(request,acid):   
        categoria=n_categorias()
        n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
        mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
        
        f = Tiendas.objects.get(pk=acid)           
       
        if request.method == 'POST':
            
            form = TiendasForm(request.user.username,request.POST,request.FILES,instance=f)
       
            if form.is_valid():
                   tiendecilla = form.save(commit=False)
                   # commit=False tells Django that "Don't send this to database yet.
                   # I have more things I want to do with it."
                   tiendecilla.ultima_fecha_edicion=datetime.datetime.now()             
                   tiendecilla.save() # Now you can send it to DB
                   form.save() 
                   connection.close()
                   return render(request,'confirmar.html',locals())             
                    
        else:
            
            form = TiendasForm(request.user.username,instance=f)
            

        
        connection.close()
        #return render_to_response('formulario.html', locals(),context_instance=RequestContext(request))
        return render(request,'formulario_ingreso.html',locals())   




def mi_tienda(request,idusuario,nombretienda):
    
    categoria=categorizar(idusuario,nombretienda)
    
    tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first() 
    visitas=tiendas.n_visitas

    tiendas.n_visitas+=1      
    tiendas.save()


    
    var=tiendas.codigoapk    

    productos=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__contains=nombretienda)).order_by("precio_A")[:10]
    
    connection.close() 
    return render(request,'catalogo_tienda.html',locals())   
 
def mis_tiendas(request,idusuario):
  
      categoria=n_categorias()
      n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
      mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
      
      tiendas=Tiendas.objects.filter(id_usuario=idusuario)
      connection.close()
    
      return render(request,'catalogo.html',locals())   




#def mis_productos(request,nombre): 
   # productos=Productos.objects.filter(id_usuario=nombre) 
  
  
 # return render(request,'principal_tienda.html',locals())   


def ver_categorias(request,item):
  
  categoria=n_categorias()
  n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
  mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
  
   

  if item=="xproductox":
    productos=Productos.objects.all()
  elif item=="xcomerciox":
    comercio=Ccomercial.objects.all()
  elif item=="xtiendax":
    tiendas=Tiendas.objects.all()
   
  else:  
    tiendas=Tiendas.objects.filter(categoria__categoria__contains=item)  
    productos=Productos.objects.filter(categoria__categoria__contains=item)    
    
  
  connection.close()


  #return render_to_response('catalogo.html',locals(),context_instance=RequestContext(request))
  return render(request,'catalogo.html',locals())   

    
def ver_mis_categorias(request,idusuario,nombretienda,item):
  
  categoria=categorizar(idusuario,nombretienda)
  
  tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()

  if item=="xproductox":    
    productos=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__contains=nombretienda)) 

    
  else:      
    productos=Productos.objects.filter(Q(categoria__categoria__contains=item) & Q(tienda__nombre_tienda__contains=nombretienda)) 
   
   
  connection.close()
  #return render_to_response('catalogo.html',locals(),context_instance=RequestContext(request))
  return render(request,'catalogo_tienda.html',locals())   
 
def busqueda_tienda(request,idusuario,nombretienda):
     
     categoria=categorizar(idusuario,nombretienda)
     
     if request.POST:
        palabra = request.POST.get('nombre')
        #guarda la palabra buscada siempre y cuando no exista EN EL REGISTRO DE BUSQUEDA
        if Buscar.objects.filter(id_usuario=request.user.username,item_de_busqueda=palabra).count() <= 0:
            busqueda=Buscar(id_usuario=request.user.username,item_de_busqueda=palabra)
            busqueda.save()
        
        tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()
        productos= Productos.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra) & Q(tienda__nombre_tienda__contains=nombretienda))
        connection.close()
        return render(request,'catalogo_tienda.html',locals()) 

def busqueda(request):
     categoria=n_categorias()
     n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
     mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
     
     if request.POST:
        palabra = request.POST.get('nombre')
        #guarda la palabra buscada siempre y cuando no exista EN EL REGISTRO DE BUSQUEDA
        if Buscar.objects.filter(id_usuario=request.user.username,item_de_busqueda=palabra).count() <= 0:
            fecha=datetime.datetime.now()
            busqueda=Buscar(id_usuario=request.user.username,item_de_busqueda=palabra,fecha_busqueda=fecha)
            busqueda.save()



        productos= Productos.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra))
        tiendas= Tiendas.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre_tienda__icontains=palabra) | Q(descripcion__icontains=palabra))
        comercio= Ccomercial.objects.filter(Q(nombre_ccomercial__icontains=palabra) | Q(ubicacion__icontains=palabra) | Q(descripcion_ccomercial__icontains=palabra)) 
     

       
     connection.close()
     return render(request,'catalogo.html',locals())   
                  
   

import datetime
#@login_required
def pagina_principal(request):   


                         n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
                         categoria=n_categorias()
                         
                         mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username) 
                         configurar=Configuracion_sistema.objects.all().first()
                         
                         configurar.n_visitas+=1         
                         configurar.save()

                         
                         try:
                             comercio,tiendas,productos=publicida_inteligencia(request)
                         except:
                             pass
                         nuevo_comercio=Ccomercial.objects.all().order_by("-id")[:6]
                         nuevas_tiendas=Tiendas.objects.all().order_by("-id")[:6]
                         nuevos_productos=Productos.objects.all().order_by("-id")[:6]
                         
                         try:
                            count = Tiendas.objects.all().count()
                            rand_ids = sample(range(1, count), 3)
                            aleatorias_tiendas=Tiendas.objects.filter(id__in=rand_ids)
                         except:
                             pass
                         try:                      
                            count = Productos.objects.all().count()
                            rand_ids = sample(range(1, count), 3)
                            aleatorias_productos=Productos.objects.filter(id__in=rand_ids)
                         except:
                             pass

                         try:                      
                            count = Ccomercial.objects.all().count()
                            rand_ids = sample(range(1, count), 3)
                            aleatorias_comercio=Ccomercial.objects.filter(id__in=rand_ids)
                         except:
                             pass

                         
                         

                         connection.close()                    
                         return render(request,'principal.html',locals())   



def catalogo(request, var):
  categoria=n_categorias()
  n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
  mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)

  #return render_to_response('catalogo.html', locals(),context_instance=RequestContext(request))
  connection.close()
  return render(request,'catalogo.html',locals())   

def informacion(request):
  categoria=n_categorias()
  n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
  mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
  #return render_to_response('informacion.html', locals(),context_instance=RequestContext(request))
  connection.close()
  return render(request,'informacion.html',locals())   

def informacion_vendedor(request,idusuario):
      categoria=n_categorias()
      n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
     

      usuario=Usuarios.objects.filter(id_usuario=idusuario).first()
      cantidad_tiendas=Tiendas.objects.filter(id_usuario=idusuario).count()    
      tiendas=Tiendas.objects.filter(id_usuario=idusuario)
      connection.close()
      
      return render(request,'informacion_vendedor.html',locals())   



from mysite.datos_artetronica.cart import Cart

@login_required

def add_to_cart(request,product_id,idusuario,nombretienda):    
    
    categoria=n_categorias()
    n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
    mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)

    quantity= request.POST.get("cant")
    productos = Productos.objects.get(id=product_id)
    
    precio=productos.precio_A   
    if precio==None:
      precio=0

    
    cart = Cart(request)
    cart.add(productos, precio, quantity)
    total=cart.summary()    
   
    connection.close()
    return render(request,'confirmar_tienda.html',locals())   
    
@login_required
def remove_from_cart(request, product_id):
    categoria=n_categorias()
    n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
    mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)

    product = Productos.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    connection.close()

@login_required
def get_cart(request,bandera,idusuario,nombretienda):
   
    categoria=categorizar(idusuario,nombretienda)
    
    tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()
      
    duenotienda=Usuarios.objects.filter(id_usuario=idusuario).first()
    
    cliente=Usuarios.objects.filter(id_usuario=request.user.username).first()

    cart = Cart(request)
    cart.view()
    total=cart.summary()   
  
    mensaje_pedido=""
    for item in cart:  
            mensaje_pedido+=str(item.quantity)+"---" + str(item.product)+"---"+str(item.unit_price)+"---"+ str(item.total_price)+ "\n"
    
    mensaje_pedido+= "\n$ "+str(total) 

    
    if bandera=="1":
            mensaje="Hola, somos xgangas y registramos que su tienda :\n"
            mensaje+= str(nombretienda)+ " y No. de contacto" +str(duenotienda.id_usuario)  +"\n"
            mensaje+="tubo una visita y el cliente se intereso por esto::\n"
            
            for item in cart:     
                 mensaje+= "["+str(item.quantity)+str(item.product )+str(item.total_price)+"]\n"
            
            mensaje+="\nEl total es:"+str(total)+"\n\n"
            
            whatsapp=cliente.id_usuario
            fecha= datetime.datetime.now()

            mensaje+="El numero de contacto del cliente es:"+str(cliente.id_usuario)+"\n"
            mensaje+="El Nombre del cliente es:"+str(cliente.nombre)+"\n"
            mensaje+="El Email del cliente es:"+str(cliente.mail)+"\n"

            mensaje+= str(fecha)
            sender =duenotienda.email
            asunto="de Xgangas: negocios"
            try:
               send_mail(asunto, mensaje,"xgangasx@gmail.com",(sender,), fail_silently=False) 
            except:
                pass            
            connection.close()
            return render(request,'confirmar_tienda.html',locals())               
    else:

            #return render_to_response('carrito.html', locals(),context_instance=RequestContext(request))
          connection.close() 
          return render(request,'carrito.html',locals())   


@login_required
def cambiar_estado_pedido(request,idusuario,nombretienda,id_del_pedido):  

                        categoria=categorizar(idusuario,nombretienda)

                        tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()                  

                        ped = Pedidos.objects.get(pk=id_del_pedido)
                                                                       
                        if ped.estado=="ENCARGADO":
                             ped.estado="PRODUCCION"
                        
                        elif ped.estado=="PRODUCCION":
                              ped.estado="EMPACADO"
                        
                        elif ped.estado=="EMPACADO":
                              ped.estado="ENTREGADO"

                        elif ped.estado=="ENTREGADO":
                              ped.estado="ENCARGADO"
 
                        else:
                          pass 
                       
                        ped.save() # Guardar los datos en la base de datos 
                        #bandera=ped.estado_del_pedido 
                        #pedidos=Pedido.objects.filter(estado_del_pedido=bandera) 
                        i=ped
                        connection.close()
                        return render(request,'catalogo_pedidos.html',locals())

@login_required
def editar_pedido(request,idusuario,nombretienda,acid): 
        categoria=categorizar(idusuario,nombretienda)

        tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()   
        
        f = Pedidos.objects.get(pk=acid)           
       
        if request.method == 'POST':
            form = PedidosForm(request.POST,request.FILES,instance=f)
       
            if form.is_valid():
                    ped=form.save(commit=False)
                    ped.id_usuario =  request.user.username
                    ped.save() # Guardar los datos en la base de datos 
                    connection.close()
                    return render(request,'confirmar_tienda.html',locals())

        else:
            
            form = PedidosForm(instance=f)   
        
        connection.close()
        return render(request,'pedido.html',locals())


@login_required
def hacer_pedido(request,idusuario,nombretienda): 
        categoria=categorizar(idusuario,nombretienda)
        
        tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()


        if request.method == 'POST': # si el usuario est enviando el formulario con datos
            
                    form = PedidosForm(request.POST,request.FILES)   
                    if form.is_valid():

                        ped=form.save(commit=False)
                        ped.id_usuario = request.user.username
                        ped.save() # Guardar los datos en la base de datos 
                        connection.close()
                        return render(request,'confirmar_tienda.html',locals())
        else:            
                       
                        form = PedidosForm()                

        connection.close() 
        return render(request,'pedido.html',locals())

     
     
        #return render_to_response('formulario.html', locals() ,context_instance=RequestContext(request))
@login_required
def listado_pedido(request,idusuario,nombretienda,bandera): 

    categoria=categorizar(idusuario,nombretienda)
     
    tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()
    var=tiendas.codigoapk
    #try:
    #    usuario=Usuarios.objects.filter(id_usuario=request.user.username).first() 
    #    var=usuario.codigoapk     
    #except:
    #    pass

    if bandera=="TODOS":
        pedidos= Pedidos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda=nombretienda)).order_by("fecha_de_entrega")
    
    else:                   
        pedidos= Pedidos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda=nombretienda) & Q(estado=bandera)).order_by( "fecha_de_entrega")
    connection.close() 
    return render(request,'catalogo_pedidos.html',locals())
        


def carrusel(request,id_prod,idusuario,nombretienda):
     categoria=categorizar(idusuario,nombretienda)     
     tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()

     productos=Productos.objects.get(id=id_prod)
     connection.close()
     return render(request,'carrusel2.html',locals())

def carrusel_pedidos(request,id_prod,idusuario,nombretienda):
     



     categoria=categorizar(idusuario,nombretienda)     
     tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()

     productos=Pedidos.objects.get(id=id_prod)
     connection.close()
     return render(request,'carrusel2.html',locals())

      
            
            
    




def cambiar_estado_tienda(request,idusuario,id_dela_tienda,estado):
                        categoria=n_categorias()
                        n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()                           
                       
                        tiend = Tiendas.objects.get(pk=id_dela_tienda)
                                                                       
                        if estado=="DISPONIBLE" or estado=="NO_DISPONIBLE":
                             tiend.estado_tienda=estado
                             tiend.save()
                                              
                         # Guardar los datos en la base de datos 
                        
                        tiendas=[]
                        tiendas.append(tiend)
                        connection.close()
                        return render(request,'catalogo.html',locals())

def cambiar_estado_producto(request,idusuario,nombretienda,id_del_producto,estado_nuevo):  

                        categoria=categorizar(idusuario,nombretienda)

                        tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()                  

                        prod = Productos.objects.get(pk=id_del_producto)
                                                                       
                        if estado_nuevo=="EN_EXISTENCIA" or estado_nuevo=="AGOTADO" or estado_nuevo=="SOLO_POR_ENCARGO" or estado_nuevo=="EN_PRODUCCION" or estado_nuevo=="VENDIDO":
                             prod.estado_prod=estado_nuevo
                             prod.save()
                                              
                         # Guardar los datos en la base de datos 
                        i=prod
                        productos=[]
                        productos.append(prod)
                        connection.close()
                        return render(request,'catalogo_tienda.html',locals())


def descargar(request,idusuario,nombretienda,id_del_producto):  

                        categoria=categorizar(idusuario,nombretienda)

                        tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()                  

                        prod = Productos.objects.get(pk=id_del_producto)
                        clave= request.POST.get("descargar")                                               
                        
                        if prod.password_de_recurso==clave:                            
                             bandera="CORRECTO"
                        else:
                             
                             bandera="INCORRECTO"                 
                         # Guardar los datos en la base de datos 
                        
                        connection.close()
                        return render(request,'descarga.html',locals())                     





def centro_comercial(request,idusuario,nombre_del_centro_comercial):
    categoria=n_categorias()
    n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()        
    
    tiendas= Tiendas.objects.filter(Q(ccomercial__nombre_ccomercial__icontains=nombre_del_centro_comercial))

    ccomercial=Ccomercial.objects.filter(id_usuario=idusuario,nombre_ccomercial=nombre_del_centro_comercial).first()
    
    connection.close()
    return render(request,'catalogo.html',locals())   


       

def agregar_producto_al_carrito(request,id_del_producto):   
    categoria=n_categorias()
    mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
    n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
    
    el_producto=Productos.objects.get(id=id_del_producto)

    lafecha=datetime.datetime.now()     

    if request.POST:
            cant = request.POST.get("cant")
            espe = request.POST.get('especificacion')

            #guarda la palabra buscada siempre y cuando no exista EN EL REGISTRO DE BUSQUEDA
            cant=str(cant)
            cant=eval(cant) 


            if cant>0:
                 
                 try: 
                    total_x=cant*el_producto.precio_A
                 except: 
                    total_x
               
                      
                 #carrito=Carro_de_compras(id_usuario=request.user.username,id_vendedor=el_producto.id_usuario,id_producto=id_del_producto,nombre_tienda=el_producto.tienda.nombre_tienda,cantidad=cant,nombre=el_producto.nombre,precio=el_producto.precio_A,total=total_x,especificacion=espe,estado_prod="QUIERO_PEDIR_ESTO" ,fecha_ingreso=lafecha)
                 carrito=Carro_de_compras(producto=el_producto,id_comprador=request.user.username,cantidad=cant,total=total_x,especificacion=espe,estado_prod="QUIERO_PEDIR_ESTO" ,fecha_ingreso=lafecha)
                 
                 carrito.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def contador_de_productos_carrito(el_usuario):

    if el_usuario=="EL_COMPRRADOR":

             npquiero= Carro_de_compras.objects.filter(id_comprador=request.user.username,estado_prod="QUIERO_PEDIR_ESTO").count()
             nprecibidop= Carro_de_compras.objects.filter(id_comprador=request.user.username,estado_prod="EL_VENDEDOR_RECIBIO_EL_PEDIDO").count()
             npconfirmado= Carro_de_compras.objects.filter(id_comprador=request.user.username,estado_prod="EL_VENDEDOR_A_CONFIRMADO").count()
             npentregado= Carro_de_compras.objects.filter(id_comprador=request.user.username,estado_prod="PRODUCTO_ENTREGADO").count()
             nprecibi= Carro_de_compras.objects.filter(id_comprador=request.user.username,estado_prod="RECIBI_EL_PRODUCTO").count()
             N_pedido=npquiero+nprecibidop+npconfirmado+npentregado 
             
    elif el_usuario=="EL_VENDEDOR":
      
             npquiero= Carro_de_compras.objects.filter(producto__id_usuario=request.user.username,estado_prod="QUIERO_PEDIR_ESTO").count()
             nprecibidop= Carro_de_compras.objects.filter(producto__id_usuario=request.user.username,estado_prod="EL_VENDEDOR_RECIBIO_EL_PEDIDO").count()
             npconfirmado= Carro_de_compras.objects.filter(producto__id_usuario=request.user.username,estado_prod="EL_VENDEDOR_A_CONFIRMADO").count()
             npentregado= Carro_de_compras.objects.filter(producto__id_usuario=request.user.username,estado_prod="PRODUCTO_ENTREGADO").count()
             nprecibi= Carro_de_compras.objects.filter(producto__id_usuario=request.user.username,estado_prod="RECIBI_EL_PRODUCTO").count()
             N_pedido=npquiero+nprecibidop
    else:
             npquiero= 0
             nprecibidop= 0
             npconfirmado= 0
             npentregado= 0
             nprrecibi= 0
             N_pedido=0
    
    return N_pedido
             


def ver_el_carrito(request,estado_del_producto,el_usuario):
      categoria=n_categorias()
      mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
      n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina() 
      el_usuario_x=el_usuario
      
      if estado_del_producto=="TODOS":
          
          if el_usuario_x=="EL_COMPRRADOR":
             carrito= Carro_de_compras.objects.filter(id_comprador=request.user.username).order_by("producto__tienda__nombre_tienda")
          else:
             carrito= Carro_de_compras.objects.filter(producto__id_usuario=request.user.username).order_by("producto__tienda__nombre_tienda")



      else:

          if el_usuario_x=="EL_COMPRRADOR":
             carrito= Carro_de_compras.objects.filter(id_comprador=request.user.username,estado_prod=estado_del_producto).order_by("producto__tienda__nombre_tienda")
             if estado_del_producto=="QUIERO_PEDIR_ESTO":
                  gran_total=0
                  for i in carrito:
                        gran_total = gran_total + i.total
          else:
            carrito= Carro_de_compras.objects.filter(producto__id_usuario=request.user.username,estado_prod=estado_del_producto).order_by("producto__tienda__nombre_tienda")
            gran_total=0
            for i in carrito:
                        gran_total = gran_total + i.total

      return render(request,'ver_carrito_de_compras.html',locals())   


def eliminar_producto_del_carrito(request,id_producto):
       categoria=n_categorias()
       mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
       n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()

       Carro_de_compras.objects.get(id=id_producto).delete()
       carrito= Carro_de_compras.objects.filter(id_comprador=request.user.username).order_by("producto__tienda__nombre_tienda")
    
       #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
       return render(request,'ver_carrito_de_compras.html',locals()) 


def editar_producto_del_carrito(request,id_producto):  
       categoria=n_categorias()
       mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
       n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()

       f = Carro_de_compras.objects.get(pk=id_producto)           
       
       if request.method == 'POST':
            
                form = Carro_de_comprasForm(request.POST,request.FILES,instance=f)
                      
                if form.is_valid():                         
         
                            form.save()
                            try:
                                 f.total=f.cantidad*f.producto.precio_A 
                            except:
                                 f.total=0
                            f.save()                                 
                  
                connection.close()  
                carrito= Carro_de_compras.objects.filter(id_comprador=request.user.username).order_by("producto__tienda__nombre_tienda")
                              
                return render(request,'ver_carrito_de_compras.html',locals())                                                  
                
       else:           
              
              form = Carro_de_comprasForm(instance=f)
             

        
       connection.close()
       #return render_to_response('formulario.html', locals(),context_instance=RequestContext(request))
       return render(request,'editar_carrito_de_compras.html',locals())   


def editar_estado_producto_del_carrito(request,id_producto,el_usuario):  
       categoria=n_categorias()
       mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
       n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()

       f = Carro_de_compras.objects.get(pk=id_producto) 

       if el_usuario=="EL_VENDEDOR":                

             if f.estado_prod=="QUIERO_PEDIR_ESTO":
                  f.estado_prod="EL_VENDEDOR_RECIBIO_EL_PEDIDO"     

             elif f.estado_prod=="EL_VENDEDOR_RECIBIO_EL_PEDIDO":
                  f.estado_prod="EL_VENDEDOR_A_CONFIRMADO"   

             elif f.estado_prod=="EL_VENDEDOR_A_CONFIRMADO":
                   f.estado_prod="PRODUCTO_ENTREGADO"
             else:
                 pass 
             
             estado_del_producto=f.estado_prod
             f.save()
             carrito= Carro_de_compras.objects.filter(producto__id_usuario=request.user.username,estado_prod=estado_del_producto).order_by("producto__tienda__nombre_tienda")
     
       elif el_usuario=="EL_COMPRADOR": 

            if f.estado_prod=="PRODUCTO_ENTREGADO":
                   f.estado_prod=="PRODUCTO_RECIBIDO_YA!"
            estado_del_producto=f.estado_prod
            f.save()
            carrito= Carro_de_compras.objects.filter(id_comprador=request.user.username,estado_prod=estado_del_producto).order_by("producto__tienda__nombre_tienda")

       else:
                 pass
     
       connection.close()                
       return render(request,'ver_carrito_de_compras.html',locals())



def realizar_compra(request):
     categoria=n_categorias()
     mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
     n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()

     carrito= Carro_de_compras.objects.filter(id_comprador=request.user.username,estado_prod="QUIERO PEDIR ESTO").order_by("producto__tienda__nombre_tienda")
     
     for  i in carrito:
        i.estado_prod="EL_VENDEDOR_RECIBIO_EL_PEDIDO"
        i.save()         

     return render(request,'confirmar_la_venta.html',locals())   



def realizar_compra_individual(request,id_producto):
     categoria=n_categorias()
     mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
     n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()

     carrito= Carro_de_compras.objects.get(id=id_producto)
     carrito.estado_prod="EL_VENDEDOR_RECIBIO_EL_PEDIDO" 
     carrito.save() 
     
     return render(request,'confirmar_compra.html',locals())   






def enviar_mensaje(request,id_del_producto): 
    categoria=n_categorias()
    mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
    n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
    
    producto_x=Productos.objects.get(id=id_del_producto)
   
    if request.POST:           
            coment = request.POST.get('comentario')

            #if request.user.username:
            ncontacto=request.user.username
            la_respuesta="Gracias, le contactarenmos a la brevedad"
            lafecha=datetime.datetime.now()
            mensaje=Mensajes(producto=producto_x,contacto=ncontacto,pregunta=coment,respuesta=la_respuesta,estado_mensaje="NUEVO",fecha=lafecha)
            
            mensaje.save()
            
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
                  

def ver_mis_mensajes(request,estado_mensaje,el_usuario):                
               
                categoria=n_categorias()
                mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)                
                n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()

                el_usuario_x=el_usuario  
                if el_usuario_x=="EL_VENDEDOR":
                            if estado_mensaje=="NUEVO":
                                  mensajes=Mensajes.objects.filter(producto__id_usuario=request.user.username,estado_mensaje=estado_mensaje).order_by("contacto")                
                            
                            elif estado_mensaje=="ATENDIDO": 
                                  mensajes=Mensajes.objects.filter(producto__id_usuario=request.user.username,estado_mensaje=estado_mensaje).order_by("contacto")                
                            
                            else:
                                 mensajes=Mensajes.objects.filter(producto__id_usuario=request.user.username).order_by("contacto")                

                elif el_usuario_x=="EL_COMPRADOR":
                            if estado_mensaje=="NUEVO":
                                  mensajes=Mensajes.objects.filter(contacto=request.user.username,estado_mensaje=estado_mensaje).order_by("producto__id_usuario")                
                            
                            elif estado_mensaje=="ATENDIDO": 
                                  mensajes=Mensajes.objects.filter(contacto=request.user.username,estado_mensaje=estado_mensaje).order_by("producto__id_usuario")                
                            
                            else:
                                 mensajes=Mensajes.objects.filter(contacto=request.user.username).order_by("producto__id_usuario")                
                else:
                  pass





                connection.close()
                return render(request,'mensajes.html',locals())   


def responder_mensaje(request,id_mensaje):
     categoria=n_categorias()
     n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina()
     mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
     
     f = Mensajes.objects.get(pk=id_mensaje)

     resp = request.POST.get('respuesta')     
     f.respuesta=resp

     f.estado_mensaje="ATENDIDO"
     f.save()


     return render(request,'mensajes.html',locals())


 














  