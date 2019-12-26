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


from django.contrib.auth.models import User  
from django.core.mail import send_mail
#from templates import *
from django.db.models import Q



from django.db import connection

from random import sample



def crear_categorias(request):
  #categorias=["Productos Ventas Varias","Alimentos bebidas","Antiguedades artesanias Adornos","Mascotas acsesorios veterinarios",
  #              "Bienes raices alquileres ventas","Tecnologia informatica informacion","Educacion ciencia Academias",
  #              "Deportes ocio acsesorios","Herramientas maquinaria equipo","Agro ferreteria maderas","Materias primas varias",
  #              "Mateiales de construccion","Muebles electrodomesticos","Productos para el hogar","Productos de consumo diario",
  #              "Productos para la industria","Industria acsesorios repuestos","Ropa Moda calzado","Salud belleza",
  #              "Usados de todos","Vehiculos acsesorios repuestos","Productos y Sevicios varios","Servicios domesticos",
  #              "Servicios personales","Servicios pofesionales","Servicios de Ensenanza","Sevicios financieros",
  #              "Servicios publicitarios","Servicio de reparaiones","Servicio de hotel alojamiento","Otros Servicios"]
  
  #for i in categorias:
  #    cat=Categoria_global(categoria=i)
  #    cat.save()


  conf=Configuracion_sistema(mensaje_bienvenida="Bienvenido a DETODONEGOCIO, Has tu compra, nosotros financiamos el 50% Inicial de la compra", n_visitas=0)
  conf.save()
  
 

  

  
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

def cerrado?abierto():

  




def info_pagina(requesta):
    cantidad_usuarios=Usuarios.objects.all().count()
    cantidad_tiendas=Tiendas.objects.all().count()
    cantidad_productos=Productos.objects.all().count()

    
    try:
          cantidad_pedidos=Carro_de_compras.objects.filter(id_comprador=requesta.user.username).filter(estado_prod="QUIERO_PEDIR_ESTO").count()+Carro_de_compras.objects.filter(producto__id_usuario=request.user.username).filter(estado_prod="QUIERO_PEDIR_ESTO").count()
    except:  
          cantidad_pedidos=Carro_de_compras.objects.all().count()

          
    try:
          el_usuario=Usuarios.objects.get(id_usuario=requesta.user.username)
          t_usuario=el_usuario.tipo_usuario
          t_ciudad=el_usuario.estoy_en
    except:  
          t_usuario="EL_COMPRADOR"
          t_ciudad="TODOS"


    connection.close()
    cantidad_mensajes=0  
    return t_ciudad,t_usuario,cantidad_usuarios, cantidad_tiendas, cantidad_productos,cantidad_pedidos,cantidad_mensajes



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
     elif  usuario.plan_tienda_activo=="CINCOMIL" and cantidad_productos<5000:
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


def publicida_inteligencia(request,ciudad):
    
    items=Buscar.objects.filter(id_usuario=request.user.username).order_by("-fecha_busqueda").first()
    palabra=items.item_de_busqueda

    if ciudad=="TODOS":  
          
          productos= Productos.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra)).order_by("tienda__plan_publicidad_activo")[:6]
          tiendas= Tiendas.objects.filter(Q(categoria__icontains=palabra) | Q(nombre_tienda__icontains=palabra) | Q(descripcion__icontains=palabra)).order_by("plan_publicidad_activo")[:6]
          comercio= Ccomercial.objects.filter(Q(nombre_ccomercial__icontains=palabra) | Q(ubicacion__icontains=palabra) | Q(descripcion_ccomercial__icontains=palabra)).order_by("plan_publicidad_activo")[:3] 
    else:
          productos= Productos.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra)).filter(tienda__ubicacion=ciudad).order_by("plan_publicidad_activo")[:6]
          tiendas= Tiendas.objects.filter(Q(categoria__icontains=palabra) | Q(nombre_tienda__icontains=palabra) | Q(descripcion__icontains=palabra)).filter(ubicacion=ciudad).order_by("plan_publicidad_activo")[:6]
          comercio= Ccomercial.objects.filter(Q(nombre_ccomercial__icontains=palabra) | Q(ubicacion__icontains=palabra) | Q(descripcion_ccomercial__icontains=palabra)).filter(ubicacion=ciudad).order_by("plan_publicidad_activo")[:3] 


    connection.close()       
    return  comercio,tiendas,productos

@login_required
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
        
        ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)
        mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)

        import os, sys
       
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
               
              
                    form = UsuariosForm(request.POST,request.FILES)                      
                    
                    if form.is_valid() :                        
                            
                            whatsapp = form.cleaned_data['id_usuario']
                            contra = form.cleaned_data['clave'] 
                            nombr=form.cleaned_data['nombre']
                            apellid=form.cleaned_data['apellido']
                                          
                            
                            user = User.objects.create_user(username=whatsapp, password=contra, first_name=nombr ,last_name=apellid)
                            user.save() 
                            
                                                       
                            usuario = form.save(commit=False)
                            usuario.id_usuario = user.username # Set the user object here
                            usuario.save() # Now you can send it to DB
                            
                            form.save() 

                            
                            connection.close()
                            return render(request,'confirmar_usuario.html',locals())                  
                

        else:            
                         
                         form=UsuariosForm()
        connection.close()                  
        return render(request,'formulario_crear_usuario.html',locals()) 

        
@login_required
def editar_usuario(request):   
             categoria=n_categorias()
             ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)
             mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
          
             f = Usuarios.objects.get(id_usuario=request.user.username)           
             
             if request.method == 'POST':
                  
                  form = UsuariosForm(request.POST,request.FILES,instance=f)
             
                  if form.is_valid():

                          contra = form.cleaned_data['clave']
                          whatsapp = form.cleaned_data['id_usuario']                          
                          nombr=form.cleaned_data['nombre']
                          apellid=form.cleaned_data['apellido']
                          corre=form.cleaned_data['email']
                        

                          user = User.objects.get(username=request.user.username)
                          user.set_password(contra)
                          user.username=whatsapp
                          user.first_name=nombr
                          user.last_name=apellid
                          user.email=corre


                          user.save()

                          usu=form.save(commit=False)
                          usu.id_usuario = request.user.username
                          usu.save() # Guardar los datos en la base de datos 
                          #return render_to_response('confirmar.html',locals(),context_instance=RequestContext(request))
                          form.save() 
                          #whatsapp=request.user.username
                          #fecha= datetime.datetime.now()
                          #mensaje= str(fecha)+"  "+str(whatsapp) + "EDITO SU ESTADO "+"\n"
                          #sender =str("xgangasx@gmail.com")
                          #asunto="edita"+" "+ str(whatsapp)
                          #try:
                          #    send_mail(asunto, mensaje,"xgangasx@gmail.com",(sender,), fail_silently=False) 
                          #except:
                          #     pass        
                          connection.close()
                          return render(request,'confirmar.html',locals())             
                  
             else:
                  
                  form = UsuariosForm(instance=f)
                  

              

             connection.close()
             #return render_to_response('formulario.html', locals(),context_instance=RequestContext(request))
             

             if t_usuario=="EL_COMPRADOR" :
                  return render(request,'formulario_editar_usuario_comprador.html',locals())
             else:    
                  
                  return render(request,'formulario_editar_usuario.html',locals())


       






@login_required
def crear_tienda(request):                

     #!/usr/bin/python
     # -*- coding: latin-1 -*-
     import os, sys
     categoria=n_categorias()
     ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)
     mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username) 

     if t_usuario=="EL_ADMINISTRADOR" or t_usuario=="EL_VENDEDOR":
    
           if request.method == 'POST': # si el usuario est enviando el formulario con datos
                  form=TiendasForm(request.user.username,request.POST,request.FILES)                   
                        
                  if form.is_valid():
                                nombretienda = form.cleaned_data['nombre_tienda']
                                tiendecilla = form.save(commit=False)
                                # commit=False tells Django that "Don't send this to database yet.
                                # I have more things I want to do with it."
                                tiendecilla.id_usuario = request.user.username # Set the user object here             
                                                 
                                tiendecilla.save() # Now you can send it to DB
                                form.save()  
                                connection.close()
                                #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                                tiendas=Tiendas.objects.filter(id_usuario=request.user.username,nombre_tienda=nombretienda).first() 
                              
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
     

     else:

          return render(request,'sin_autorizacion.html',locals())





@login_required
def editar_tienda(request,acid):   
        categoria=n_categorias()
        ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)
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

    try:
        corazon=Preferidas.objects.filter(id_comprador=request.user.username,tienda__id=tiendas.id).count()
        if corazon>0:
            corazon="PREFERIDA"
        else:
            corazon="NO_PREFERIDA"
    except:
        corazon="NO_PREFERIDA"
    
    var=tiendas.codigoapk    

    productos=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__icontains=nombretienda)).order_by("precio_A")[:10]
    
    try:
        comprador=Usuarios.objects.get(id_usuario=request.user.username) 
        connection.close()
        if comprador.tipo_de_vista=="NORMAL":
             return render(request,'catalogo_tienda.html',locals())   
        elif comprador.tipo_de_vista=="LINEAL":
             return render(request,'catalogo_tienda_lineal.html',locals())   
        else:
             return render(request,'catalogo_tienda_fotitos.html',locals()) 
    except:
        return render(request,'catalogo_tienda.html',locals())    
 

@login_required
def mis_tiendas(request,idusuario):
  
      categoria=n_categorias()
      ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)
      mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)

     
      
      if t_usuario=="EL_ADMINISTRADOR" or t_usuario=="EL_VENDEDOR":

                tiendas=Tiendas.objects.filter(id_usuario=idusuario)
                connection.close()
    
                return render(request,'catalogo.html',locals())   
      else:
                   return render(request,'sin_autorizacion.html',locals())



#def mis_productos(request,nombre): 
   # productos=Productos.objects.filter(id_usuario=nombre) 
  
  
 # return render(request,'principal_tienda.html',locals())   


def ver_categorias(request,item):
  
  categoria=n_categorias()
  ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)
  mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)


   

  if item=="xproductox":
    productos=Productos.objects.all()
  elif item=="xcomerciox":
    comercio=Ccomercial.objects.all()
  elif item=="xtiendax":
    tiendas=Tiendas.objects.all()
   
  else:  
    tiendas=Tiendas.objects.filter(categoria__icontains=item)  
    productos=Productos.objects.filter(categoria__categoria__icontains=item)    
    
  
  connection.close()


  #return render_to_response('catalogo.html',locals(),context_instance=RequestContext(request))
  return render(request,'catalogo.html',locals())   

@login_required    
def ver_mis_categorias(request,idusuario,nombretienda,item):
  
  categoria=categorizar(idusuario,nombretienda)
  
  tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()
  corazon=Preferidas.objects.filter(id_comprador=request.user.username,tienda__id=tiendas.id).count()
  if corazon>0:
        corazon="PREFERIDA"
  else:
        corazon="NO_PREFERIDA"

  if item=="xproductox":    
    productos=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__icontains=nombretienda)) 

    
  else:      
    productos=Productos.objects.filter(Q(categoria__categoria__icontains=item) & Q(tienda__nombre_tienda__icontains=nombretienda)) 
   
  comprador=Usuarios.objects.get(id_usuario=request.user.username) 
  connection.close()
  if comprador.tipo_de_vista=="NORMAL":
         return render(request,'catalogo_tienda.html',locals())   
  elif comprador.tipo_de_vista=="LINEAL":
         return render(request,'catalogo_tienda_lineal.html',locals())   
  else:
         return render(request,'catalogo_tienda_fotitos.html',locals())   
  #return render_to_response('catalogo.html',locals(),context_instance=RequestContext(request))
   


@login_required
def cambiar_tipo_de_vista(request,id_dela_tienda):
      tiendas = Tiendas.objects.get(pk=id_dela_tienda)
      idusuario=tiendas.id_usuario 
      nombretienda=tiendas.nombre_tienda
      
      categoria=categorizar(idusuario,nombretienda)     
      var=tiendas.codigoapk        


      productos=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__icontains=nombretienda)).order_by("precio_A")[:10]
      comprador=Usuarios.objects.get(id_usuario=request.user.username)
                          
      corazon=Preferidas.objects.filter(id_comprador=request.user.username,tienda__id=id_dela_tienda).count()
      if corazon>0:
        corazon="PREFERIDA"
      else:
        corazon="NO_PREFERIDA"
                                                                       
      if comprador.tipo_de_vista=="NORMAL":
            comprador.tipo_de_vista="LINEAL"

      elif comprador.tipo_de_vista=="LINEAL":
            comprador.tipo_de_vista="FOTITOS"

      else:
            comprador.tipo_de_vista="NORMAL"

      
               
      comprador.save()    

      
      if comprador.tipo_de_vista=="NORMAL":
         return render(request,'catalogo_tienda.html',locals())   
      elif comprador.tipo_de_vista=="LINEAL":
         return render(request,'catalogo_tienda_lineal.html',locals())   
      else:
         return render(request,'catalogo_tienda_fotitos.html',locals())   
         
      

  
@login_required 
def busqueda_tienda(request,idusuario,nombretienda):
     
     categoria=categorizar(idusuario,nombretienda)
     
     if request.POST:
        palabra = request.POST.get('nombre')
        #guarda la palabra buscada siempre y cuando no exista EN EL REGISTRO DE BUSQUEDA
        if Buscar.objects.filter(id_usuario=request.user.username,item_de_busqueda=palabra).count() <= 0:
            busqueda=Buscar(id_usuario=request.user.username,item_de_busqueda=palabra)
            busqueda.save()
        

        tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()
        corazon=Preferidas.objects.filter(id_comprador=request.user.username,tienda__id=tiendas.id).count()
        if corazon>0:
            corazon="PREFERIDA"
        else:
            corazon="NO_PREFERIDA"

        productos= Productos.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra) & Q(tienda__nombre_tienda__icontains=nombretienda))
        connection.close()
        return render(request,'catalogo_tienda.html',locals()) 

@login_required
def busqueda(request,bandera):
     categoria=n_categorias()
     ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)
     mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)


     
     if request.POST:
        palabra = request.POST.get('nombre')
        cate_goria= request.POST.get('categoria_busqueda')
        ciudad=request.POST.get('ciudad_busqueda') 
        #guarda la palabra buscada siempre y cuando no exista EN EL REGISTRO DE BUSQUEDA

        if bandera="COMIDA":
            palabra=""
            cate_goria="Alimentos Bebidas"
            usuario=Usuarios.objects.get(id_usuario=request.user.username)
            ciudad=usuario.estoy_en

        
        if Buscar.objects.filter(id_usuario=request.user.username,item_de_busqueda=palabra).count() <= 0:
            fecha=datetime.datetime.now()
            busqueda=Buscar(id_usuario=request.user.username,item_de_busqueda=palabra,fecha_busqueda=fecha)
            busqueda.save()

        
        if palabra=="":
           
               if cate_goria=="TODOS" and ciudad=="TODOS":
                   tiendas= Tiendas.objects.all()
                   comercio= Ccomercial.objects.all()
               
               elif cate_goria=="TODOS" and ciudad!="TODOS":
                   tiendas= Tiendas.objects.filter(ubicacion=ciudad)
                   comercio= Ccomercial.objects.filter(ubicacion=ciudad)

               elif cate_goria!="TODOS" and ciudad=="TODOS":
                   tiendas= Tiendas.objects.filter(categoria=cate_goria)
               
               elif cate_goria!="TODOS" and ciudad!="TODOS":
                   tiendas= Tiendas.objects.filter(categoria=cate_goria,ubicacion=ciudad) 

               else:
                  pass    

        else:

               if cate_goria=="TODOS" and ciudad=="TODOS":
                      productos= Productos.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra))
                      tiendas= Tiendas.objects.filter(Q(categoria__icontains=palabra) | Q(nombre_tienda__icontains=palabra) | Q(descripcion__icontains=palabra))
                      comercio= Ccomercial.objects.filter(Q(nombre_ccomercial__icontains=palabra) | Q(descripcion_ccomercial__icontains=palabra))
                 
               
               elif cate_goria=="TODOS" and ciudad!="TODOS":
                    productos= Productos.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra)).filter(tienda__ubicacion=ciudad)
                    tiendas= Tiendas.objects.filter(Q(categoria__icontains=palabra) | Q(nombre_tienda__icontains=palabra) | Q(descripcion__icontains=palabra)).filter(ubicacion=ciudad)
                    comercio= Ccomercial.objects.filter(Q(nombre_ccomercial__icontains=palabra) | Q(descripcion_ccomercial__icontains=palabra)).filter(ubicacion=ciudad)
     

               elif cate_goria!="TODOS" and ciudad=="TODOS":
                    productos= Productos.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra))
                    tiendas= Tiendas.objects.filter(Q(categoria__icontains=palabra) | Q(nombre_tienda__icontains=palabra) | Q(descripcion__icontains=palabra))
                    comercio= Ccomercial.objects.filter(Q(nombre_ccomercial__icontains=palabra) | Q(descripcion_ccomercial__icontains=palabra))
               
               elif cate_goria!="TODOS" and ciudad!="TODOS":
                    productos= Productos.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra))
                    tiendas= Tiendas.objects.filter(Q(categoria__icontains=palabra) | Q(nombre_tienda__icontains=palabra) | Q(descripcion__icontains=palabra)).filter(ubicacion=ciudad)
                    comercio= Ccomercial.objects.filter(Q(nombre_ccomercial__icontains=palabra) | Q(descripcion_ccomercial__icontains=palabra)).ubicacion=ciudad       
               else:
                  pass    
     
        try:
            if ciudad!="TODOS":
               usuario=Usuarios.objects.get(id_usuario=request.user.username)
               usuario.estoy_en=ciudad
               usuario.save()
        except:  
            pass


     connection.close()
     return render(request,'catalogo.html',locals())   
                  
   

import datetime


@login_required
def configurar_vista_pagina_principal(request): 

            ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)
            categoria=n_categorias()                             
            mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username) 
            
      
            configuracion=Usuarios.objects.get(id_usuario=request.user.username)     
            
            if configuracion.tipo_vista==0:
                    configuracion.tipo_vista=1
                    configuracion.save()
                    
            
            else:
                    configuracion.tipo_vista=0
                    configuracion.save()
            
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))       

            








            


#@login_required
def pagina_principal(request):   


                         ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)
                         categoria=n_categorias()
                         
                         mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username) 
                         configurar=Configuracion_sistema.objects.all().first()
                         
                         configurar.n_visitas+=1         
                         configurar.save()
                         

                         
                         try:
                             comercio,tiendas,productos=publicida_inteligencia(request,ciudad)
                         except:
                             pass


                         if ciudad == "TODOS":
                               nuevo_comercio=Ccomercial.objects.all().order_by("-id")[:6]
                               nuevas_tiendas=Tiendas.objects.all().order_by("-id")[:6]
                               nuevos_productos=Productos.objects.all().order_by("-id")[:6]
                         else:
                               nuevo_comercio=Ccomercial.objects.filter(ubicacion=ciudad).order_by("-id")[:6]
                               nuevas_tiendas=Tiendas.objects.filter(ubicacion=ciudad).order_by("-id")[:6]
                               nuevos_productos=Productos.objects.filter(tienda__ubicacion=ciudad).order_by("-id")[:6]

                                                  
                        
                         try:
                            if ciudad == "TODOS":
                                  count = Tiendas.objects.all().count()
                                  rand_ids = sample(range(1, count), 3)                                  
                                  aleatorias_tiendas=Tiendas.objects.filter(id__in=rand_ids)
                            else:
                                  count = Tiendas.objects.filter(ubicacion=ciudad).count()
                                  rand_ids = sample(range(1, count), 3)                                  
                                  aleatorias_tiendas=Tiendas.objects.filter(id__in=rand_ids)


                         except:
                             pass
                        


                         try:     

                             if ciudad == "TODOS":               
                                  count = Productos.objects.all().count()
                                  rand_ids = sample(range(1, count), 3)
                                  aleatorias_productos=Productos.objects.filter(id__in=rand_ids)
                             else:
                                  ount = Productos.objects.filter(tienda__ubicacion=ciudad).count()
                                  rand_ids = sample(range(1, count), 3)
                                  aleatorias_productos=Productos.objects.filter(id__in=rand_ids)


                         except:
                             pass



                         try:    
                            if ciudad == "TODOS":                  
                                  count = Ccomercial.objects.all().count()
                                  rand_ids = sample(range(1, count), 3)
                                  aleatorias_comercio=Ccomercial.objects.filter(id__in=rand_ids)
                            
                            else:
                                  count = Ccomercial.objects.filter(ubicacion=ciudad).count()
                                  rand_ids = sample(range(1, count), 3)
                                  aleatorias_comercio=Ccomercial.objects.filter(id__in=rand_ids)

                         except:
                             pass

                         
                         

                         connection.close()   
                         a=0

                         try: 
                                configuracion=Usuarios.objects.get(id_usuario=request.user.username) 
                                a=configuracion.tipo_vista
                         except:
                                a=0

                             
            
                         if a==0:                                
                                  
                                  return render(request,'principal.html',locals())  
                          
                         else:
                                  return render(request,'principal_cuadricula.html',locals())                  
                         



def catalogo(request, var):
  categoria=n_categorias()
  ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)
  mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)

  #return render_to_response('catalogo.html', locals(),context_instance=RequestContext(request))
  connection.close()
  return render(request,'catalogo.html',locals())   

def informacion(request):
  categoria=n_categorias()
  ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)
  mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
  #return render_to_response('informacion.html', locals(),context_instance=RequestContext(request))
  connection.close()
  return render(request,'informacion.html',locals())   


def informacion_vendedor(request,idusuario):
      categoria=n_categorias()
      ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)
     

      usuario=Usuarios.objects.filter(id_usuario=idusuario).first()
      cantidad_tiendas=Tiendas.objects.filter(id_usuario=idusuario).count()    
      tiendas=Tiendas.objects.filter(id_usuario=idusuario)
      connection.close()
      
      return render(request,'informacion_vendedor.html',locals())   

def informacion_comprador(request,idusuario):
      categoria=n_categorias()
      ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)
     
      usuario=Usuarios.objects.filter(id_usuario=idusuario).first()
      connection.close()
      
      return render(request,'informacion_comprador.html',locals()) 







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
     categoria=categorizar(idusuario,nombretienda)
     corazon=Preferidas.objects.filter(id_comprador=request.user.username,tienda__id=tiendas.id).count()
     if corazon>0:
        corazon="PREFERIDA"
     else:
        corazon="NO_PREFERIDA"
    
     var=tiendas.codigoapk   

     productos=Productos.objects.get(id=id_prod)
     connection.close()
     return render(request,'carrusel2.html',locals())


def carrusel_pedidos(request,id_prod,idusuario,nombretienda):

     categoria=categorizar(idusuario,nombretienda)     
     tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()
     corazon=Preferidas.objects.filter(id_comprador=request.user.username,tienda__id=tiendas.id).count()
     if corazon>0:
        corazon="PREFERIDA"
     else:
        corazon="NO_PREFERIDA"
    
     var=tiendas.codigoapk

     productos=Pedidos.objects.get(id=id_prod)
     connection.close()
     return render(request,'carrusel2.html',locals())

               
            
    

@login_required
def cambiar_estado_tienda(request,idusuario,id_dela_tienda,estado):
                        categoria=n_categorias()
                        ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)                           
                       
                        tiend = Tiendas.objects.get(pk=id_dela_tienda)
                                                                       
                        if estado=="DISPONIBLE" or estado=="NO_DISPONIBLE":
                             tiend.estado_tienda=estado
                             tiend.save()
                                              
                         # Guardar los datos en la base de datos 
                        
                        tiendas=[]
                        tiendas.append(tiend)
                        connection.close()
                        return render(request,'catalogo.html',locals())
@login_required
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

@login_required
def descargar(request,idusuario,nombretienda,id_del_producto):  

                        categoria=categorizar(idusuario,nombretienda)

                        tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()                  

                        prod = Productos.objects.get(pk=id_del_producto)
                        clave= request.POST.get("descargar")                                               
                        clave_generada=eval(request.user.username)*2

                        #if prod.password_de_recurso==clave:
                        if clave_generada==clave:                            
                             bandera="CORRECTO"
                        else:
                             
                             bandera="INCORRECTO"                 
                         # Guardar los datos en la base de datos 
                        
                        connection.close()
                        return render(request,'descarga.html',locals())                     





def centro_comercial(request,idusuario,nombre_del_centro_comercial):
    categoria=n_categorias()
    ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)        
    
    tiendas= Tiendas.objects.filter(Q(ccomercial__nombre_ccomercial__icontains=nombre_del_centro_comercial))

    ccomercial=Ccomercial.objects.filter(id_usuario=idusuario,nombre_ccomercial=nombre_del_centro_comercial).first()
    
    connection.close()
    return render(request,'catalogo.html',locals())   



          


       
@login_required
def agregar_producto_al_carrito(request,id_del_producto,foto):     

    
    el_producto=Productos.objects.get(id=id_del_producto)

    lafecha=datetime.datetime.now()      
      
    # lafecha = lafecha.strftime("%d/%m/%Y, %H:%M:%S")
    # dd/mm/YY H:M:S format
    

    if request.POST:
            cant = request.POST.get("cant")
            espe = request.POST.get('especificacion')

            #guarda la palabra buscada siempre y cuando no exista EN EL REGISTRO DE BUSQUEDA
            cant=str(cant)
            cant=eval(cant) 

            precio=str(el_producto.precio_A)
            precio=eval(precio)


            if cant>0:
                 
                 try: 
                    total_x=cant*precio
                 except: 
                    total_x=0
               
                 n=Usuarios.objects.get(id_usuario=request.user.username)     
                 #carrito=Carro_de_compras(id_usuario=request.user.username,id_vendedor=el_producto.id_usuario,id_producto=id_del_producto,nombre_tienda=el_producto.tienda.nombre_tienda,cantidad=cant,nombre=el_producto.nombre,precio=el_producto.precio_A,total=total_x,especificacion=espe,estado_prod="QUIERO_PEDIR_ESTO" ,fecha_ingreso=lafecha)
                 carrito=Carro_de_compras(usuario_car=n,nota_vendedor=el_producto.tienda.nota_de_evaluacion,nota_comprador=n.nota_de_evaluacion,nombre_comprador=n.nombre, apellido_comprador=n.apellido,mostrar_foto=foto, producto=el_producto,id_comprador=request.user.username,cantidad=cant,total=total_x,especificacion=espe,estado_prod="QUIERO_PEDIR_ESTO" ,fecha_ingreso=lafecha)
                 
                 carrito.save()

    id_dela_tienda=el_producto.tienda.id
    tiendas = Tiendas.objects.get(pk=id_dela_tienda)
    idusuario=tiendas.id_usuario 
    nombretienda=tiendas.nombre_tienda      
    categoria=categorizar(idusuario,nombretienda)     
    var=tiendas.codigoapk    
    
    corazon=Preferidas.objects.filter(id_comprador=request.user.username,tienda__id=id_dela_tienda).count()
    if corazon>0:
        corazon="PREFERIDA"
    else:
        corazon="NO_PREFERIDA"

    productos=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__icontains=nombretienda)).order_by("precio_A")
    comprador=Usuarios.objects.get(id_usuario=request.user.username)                          
          
    if comprador.tipo_de_vista=="NORMAL":
         return render(request,'catalogo_tienda.html',locals())   
    elif comprador.tipo_de_vista=="LINEAL":
         return render(request,'catalogo_tienda_lineal.html',locals())   
    elif comprador.tipo_de_vista=="FOTITOS":
         return render(request,'catalogo_tienda_fotitos.html',locals())   
    else :
          return render(request,'catalogo_tienda.html',locals())    
    



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

@login_required     
def ver_el_carrito_personal(request,id_persona_compra):
      categoria=n_categorias()
      mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
      ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request) 
      el_usuario_x=t_usuario



      if el_usuario_x=="EL_COMPRADOR":  

            if request.user.username==id_persona_compra:              
                  carrito= Carro_de_compras.objects.filter(id_comprador=request.user.username ).order_by("estado_prod")
            else:
                  carrito= Carro_de_compras.objects.filter(id_comprador=id_persona_compra ).order_by("estado_prod")

     
      elif el_usuario_x=="EL_ADMINISTRADOR" : #es el vendedor
              carrito= Carro_de_compras.objects.filter(Q(producto__id_usuario=request.user.username)  & Q(id_comprador=id_persona_compra)).order_by("estado_prod")

      elif el_usuario_x=="EL_DELIBERY":
              carrito= Carro_de_compras.objects.filter( Q(id_comprador=id_persona_compra)).order_by("estado_prod")
      else:            
        pass                      
      
      return render(request,'ver_carrito_de_compras.html',locals()) 

    
@login_required
def ver_el_carrito_de_tienda(request,id_tienda_de_compra):
      categoria=n_categorias()
      mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
      ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request) 
      el_usuario_x=t_usuario


      if el_usuario_x=="EL_COMPRADOR":  

            if request.user.username==id_persona_compra:              
                  carrito= Carro_de_compras.objects.filter(producto__tienda__id=id_tienda_de_compra) .order_by("estado_prod")
            else:
                  carrito= Carro_de_compras.objects.filter(producto__tienda__id=id_tienda_de_compra) .order_by("estado_prod")

     
      elif el_usuario_x=="EL_ADMINISTRADOR" : #es el vendedor
              carrito= Carro_de_compras.objects.filter(Q(producto__id_usuario=request.user.username) & Q(producto__tienda__id=id_tienda_de_compra) ).order_by("estado_prod")

      elif el_usuario_x=="EL_DELIBERY":
              carrito= Carro_de_compras.objects.filter(producto__tienda__id=id_tienda_de_compra).order_by("estado_prod")
      else:            
        pass                      
      
      return render(request,'ver_carrito_de_compras.html',locals()) 


@login_required
def ver_el_carrito_personal_y_de_tienda(request,id_persona_compra,id_tienda_de_compra):
    
      categoria=n_categorias()
      mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
      ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request) 
      el_usuario_x=t_usuario



      if el_usuario_x=="EL_COMPRADOR":  

            if request.user.username==id_persona_compra:              
                  carrito= Carro_de_compras.objects.filter(Q(id_comprador=request.user.username) & Q(producto__tienda__id=id_tienda_de_compra) ).order_by("estado_prod")
            else:
                  carrito= Carro_de_compras.objects.filter(Q(id_comprador=id_persona_compra) & Q(producto__tienda__id=id_tienda_de_compra) ).order_by("estado_prod")

     
      elif el_usuario_x=="EL_ADMINISTRADOR" : #es el vendedor
              carrito= Carro_de_compras.objects.filter(Q(producto__id_usuario=request.user.username) & Q(producto__tienda__id=id_tienda_de_compra)  & Q(id_comprador=id_persona_compra)).order_by("estado_prod")

      elif el_usuario_x=="EL_DELIBERY":
              carrito= Carro_de_compras.objects.filter(Q(producto__tienda__id=id_tienda_de_compra)  & Q(id_comprador=id_persona_compra)).order_by("estado_prod")
      else:            
        pass                      
      
      return render(request,'ver_carrito_de_compras.html',locals()) 




@login_required
def ver_el_carrito(request,estado_del_producto):
      categoria=n_categorias()
      mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
      ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request) 
      el_usuario_x=t_usuario




      if el_usuario_x=="EL_COMPRADOR":
              if estado_del_producto=="TODOS":
                  carrito= Carro_de_compras.objects.filter(Q(id_comprador=request.user.username) | Q(producto__tienda__administrador_junior=request.user.username) | Q(producto__tienda__administrador_junior_1=request.user.username) | Q(producto__tienda__administrador_junior_2=request.user.username) | Q(delibery_junior=request.user.username) | Q(financista_junior=request.user.username)).order_by("producto__tienda__nombre_tienda")
              elif estado_del_producto=="NUEVO":
                  carrito= Carro_de_compras.objects.filter(Q(id_comprador=request.user.username) | Q(producto__tienda__administrador_junior=request.user.username) | Q(producto__tienda__administrador_junior_1=request.user.username) | Q(producto__tienda__administrador_junior_2=request.user.username) | Q(delibery_junior=request.user.username) | Q(financista_junior=request.user.username)).filter( Q(estado_prod='QUIERO_PEDIR_ESTO') |  Q(estado_prod='EL_VENDEDOR_RECIBIO_EL_PEDIDO')).order_by("producto__tienda__nombre_tienda")
              elif estado_del_producto=="EN_PROCESO":
                   carrito= Carro_de_compras.objects.filter(Q(id_comprador=request.user.username) | Q(producto__tienda__administrador_junior=request.user.username) | Q(producto__tienda__administrador_junior_1=request.user.username) | Q(producto__tienda__administrador_junior_2=request.user.username) | Q(delibery_junior=request.user.username) | Q(financista_junior=request.user.username)).filter(Q(estado_prod='EL_VENDEDOR_A_CONFIRMADO') | Q(estado_prod='PRODUCTO_ENTREGADO')).order_by("producto__tienda__nombre_tienda")
              elif estado_del_producto=="FINALIZADO":
                    carrito= Carro_de_compras.objects.filter(Q(id_comprador=request.user.username) | Q(producto__tienda__administrador_junior=request.user.username) | Q(producto__tienda__administrador_junior_1=request.user.username) | Q(producto__tienda__administrador_junior_2=request.user.username) | Q(delibery_junior=request.user.username) | Q(financista_junior=request.user.username)).filter(estado_prod='PRODUCTO_RECIBIDO_YA').order_by("producto__tienda__nombre_tienda")
                
              else:
                  carrito= Carro_de_compras.objects.filter(Q(id_comprador=request.user.username) | Q(producto__tienda__administrador_junior=request.user.username) | Q(producto__tienda__administrador_junior_1=request.user.username) | Q(producto__tienda__administrador_junior_2=request.user.username) | Q(delibery_junior=request.user.username) | Q(financista_junior=request.user.username)).filter( Q(estado_prod='QUIERO_PEDIR_ESTO') |  Q(estado_prod='EL_VENDEDOR_RECIBIO_EL_PEDIDO')).order_by("producto__tienda__nombre_tienda")
             
           
      elif el_usuario_x=="EL_ADMINISTRADOR" : #es el vendedor
              if estado_del_producto=="TODOS":
                  carrito= Carro_de_compras.objects.filter(Q(producto__id_usuario=request.user.username)  | Q(id_comprador=request.user.username)).order_by("producto__tienda__nombre_tienda")
              elif estado_del_producto=="NUEVO":
                  carrito= Carro_de_compras.objects.filter(Q(producto__id_usuario=request.user.username) | Q(id_comprador=request.user.username)).filter( Q(estado_prod='QUIERO_PEDIR_ESTO') |  Q(estado_prod='EL_VENDEDOR_RECIBIO_EL_PEDIDO')).order_by("producto__tienda__nombre_tienda")
              elif estado_del_producto=="EN_PROCESO":
                  carrito= Carro_de_compras.objects.filter(Q(producto__id_usuario=request.user.username) | Q(id_comprador=request.user.username)).filter(Q(estado_prod='EL_VENDEDOR_A_CONFIRMADO') | Q(estado_prod='PRODUCTO_ENTREGADO')).order_by("producto__tienda__nombre_tienda")
              elif estado_del_producto=="FINALIZADO":
                  carrito= Carro_de_compras.objects.filter(Q(producto__id_usuario=request.user.username) | Q(id_comprador=request.user.username)).filter(estado_prod='PRODUCTO_RECIBIDO_YA').order_by("producto__tienda__nombre_tienda")
                
              else:
                carrito= Carro_de_compras.objects.filter(Q(producto__id_usuario=request.user.username) | Q(id_comprador=request.user.username)).filter( Q(estado_prod='QUIERO_PEDIR_ESTO') |  Q(estado_prod='EL_VENDEDOR_RECIBIO_EL_PEDIDO')).order_by("producto__tienda__nombre_tienda")
              
             
      elif el_usuario_x=="EL_DELIBERY":
                          if estado_del_producto=="TODOS":
                              carrito= Carro_de_compras.objects.filter(Q(id_comprador=request.user.username) | Q(delibery=request.user.username)).order_by("producto__tienda__nombre_tienda")
                          elif estado_del_producto=="NUEVO":
                              carrito= Carro_de_compras.objects.filter(Q(id_comprador=request.user.username) | Q(delibery=request.user.username)).filter( Q(estado_prod='QUIERO_PEDIR_ESTO') |  Q(estado_prod='EL_VENDEDOR_RECIBIO_EL_PEDIDO')).order_by("producto__tienda__nombre_tienda")
                          elif estado_del_producto=="EN_PROCESO":
                              carrito= Carro_de_compras.objects.filter(Q(id_comprador=request.user.username) | Q(delibery=request.user.username)).filter(Q(estado_prod='EL_VENDEDOR_A_CONFIRMADO') | Q(estado_prod='PRODUCTO_ENTREGADO')).order_by("producto__tienda__nombre_tienda")
                          elif estado_del_producto=="FINALIZADO":
                              carrito= Carro_de_compras.objects.filter(Q(id_comprador=request.user.username) | Q(delibery=request.user.username)).filter(estado_prod='PRODUCTO_RECIBIDO_YA').order_by("producto__tienda__nombre_tienda")
                            
                          else:
                            carrito= Carro_de_compras.objects.filter( Q(estado_prod='QUIERO_PEDIR_ESTO') |  Q(estado_prod='EL_VENDEDOR_RECIBIO_EL_PEDIDO')).order_by("producto__tienda__nombre_tienda")
                          
      
      elif el_usuario_x=="EL_FINANCISTA":
                          if estado_del_producto=="TODOS":
                              carrito= Carro_de_compras.objects.filter(Q(id_comprador=request.user.username) | Q(financista=request.user.username)).order_by("producto__tienda__nombre_tienda")
                          elif estado_del_producto=="NUEVO":
                              carrito= Carro_de_compras.objects.filter(Q(id_comprador=request.user.username) | Q(financista=request.user.username)).filter( Q(estado_prod='QUIERO_PEDIR_ESTO') |  Q(estado_prod='EL_VENDEDOR_RECIBIO_EL_PEDIDO')).order_by("producto__tienda__nombre_tienda")
                          elif estado_del_producto=="EN_PROCESO":
                              carrito= Carro_de_compras.objects.filter(Q(id_comprador=request.user.username) | Q(financista=request.user.username)).filter(Q(estado_prod='EL_VENDEDOR_A_CONFIRMADO') | Q(estado_prod='PRODUCTO_ENTREGADO')).order_by("producto__tienda__nombre_tienda")
                          elif estado_del_producto=="FINALIZADO":
                              carrito= Carro_de_compras.objects.filter(Q(id_comprador=request.user.username) | Q(financista=request.user.username)).filter(estado_prod='PRODUCTO_RECIBIDO_YA').order_by("producto__tienda__nombre_tienda")
                            
                          else:
                            carrito= Carro_de_compras.objects.filter( Q(estado_prod='QUIERO_PEDIR_ESTO') |  Q(estado_prod='EL_VENDEDOR_RECIBIO_EL_PEDIDO')).order_by("producto__tienda__nombre_tienda")
      else:
            
        pass                      
      
      return render(request,'ver_carrito_de_compras.html',locals())   





@login_required
def eliminar_producto_del_carrito(request,id_producto):
       categoria=n_categorias()
       mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
       ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)

       Carro_de_compras.objects.get(id=id_producto).delete()
       carrito= Carro_de_compras.objects.filter(id_comprador=request.user.username).order_by("producto__tienda__nombre_tienda")
    
       #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
       return render(request,'ver_carrito_de_compras.html',locals()) 

@login_required
def editar_producto_del_carrito(request,id_producto):  
       categoria=n_categorias()
       mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
       ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)


       f = Carro_de_compras.objects.get(pk=id_producto)           
       
       if request.method == 'POST':
            
                if t_usuario=="EL_COMPRADOR":
                      form = Carro_de_comprasForm(request.POST,request.FILES,instance=f)
                elif t_usuario=="EL_DELIBERY":
                      form = Carro_de_compras_delibery_Form(request.POST,request.FILES,instance=f)
                elif t_usuario=="EL_FINANCISTA":
                      form = Carro_de_compras_financista_Form(request.POST,request.FILES,instance=f)
                else:
                      form = Carro_de_compras2Form(request.POST,request.FILES,instance=f)


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
              if t_usuario=="EL_COMPRADOR":
                    form = Carro_de_comprasForm(instance=f)
              elif t_usuario=="EL_DELIBERY":
                      form = Carro_de_compras_delibery_Form(instance=f)
              elif t_usuario=="EL_FINANCISTA":
                      form = Carro_de_compras_financista_Form(instance=f)
              else: 
                    form = Carro_de_compras2Form(instance=f)
             

        
       connection.close()
       #return render_to_response('formulario.html', locals(),context_instance=RequestContext(request))
       return render(request,'editar_carrito_de_compras.html',locals())   

@login_required
def editar_estado_producto_del_carrito(request,id_producto,el_usuario):  
       categoria=n_categorias()
       mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
       ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)

       f = Carro_de_compras.objects.get(pk=id_producto) 

       if el_usuario=="EL_VENDEDOR":                

             if f.estado_prod=="QUIERO_PEDIR_ESTO":
                  f.estado_prod="EL_VENDEDOR_RECIBIO_EL_PEDIDO"     

             elif f.estado_prod=="EL_VENDEDOR_RECIBIO_EL_PEDIDO":
                  f.estado_prod="EL_VENDEDOR_A_CONFIRMADO"   

             elif f.estado_prod=="EL_VENDEDOR_A_CONFIRMADO":
                   f.estado_prod="PRODUCTO_ENTREGADO"

             #elif f.estado_prod=="PRODUCTO_ENTREGADO":
                   #f.estado_prod="PRODUCTO_RECIBIDO"      
             else:
                 pass 

             
             estado_del_producto=f.estado_prod
             f.save()
             carrito= Carro_de_compras.objects.filter(producto__id_usuario=request.user.username,estado_prod=estado_del_producto).order_by("producto__tienda__nombre_tienda")
     
       else: #es el comprador 

            if f.estado_prod=="PRODUCTO_ENTREGADO":
                   f.estado_prod="PRODUCTO_RECIBIDO_YA"
            estado_del_producto=f.estado_prod
            f.save()
            carrito= Carro_de_compras.objects.filter(id_comprador=request.user.username,estado_prod=estado_del_producto).order_by("producto__tienda__nombre_tienda")

     
       connection.close()                
       return render(request,'ver_carrito_de_compras.html',locals())


@login_required
def realizar_compra(request):
     categoria=n_categorias()
     mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
     ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)

     carrito= Carro_de_compras.objects.filter(id_comprador=request.user.username,estado_prod="QUIERO PEDIR ESTO").order_by("producto__tienda__nombre_tienda")
     
     for  i in carrito:
        i.estado_prod="EL_VENDEDOR_RECIBIO_EL_PEDIDO"
        i.save()         

     return render(request,'confirmar_compra.html',locals())   


@login_required
def realizar_compra_individual(request,id_producto):
     categoria=n_categorias()
     mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
     ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)

     carrito= Carro_de_compras.objects.get(id=id_producto)
     carrito.estado_prod="EL_VENDEDOR_RECIBIO_EL_PEDIDO" 
     carrito.save() 
     
     return render(request,'confirmar_compra.html',locals())   



def enviar_mensaje(request,id_del_producto): 
    categoria=n_categorias()
    mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
    ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)
    
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
                ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)

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
     ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request)
     mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
     
     f = Mensajes.objects.get(pk=id_mensaje)

     resp = request.POST.get('respuesta')     
     f.respuesta=resp

     f.estado_mensaje="ATENDIDO"
     f.save()


     return render(request,'mensajes.html',locals())

@login_required
def agregar_a_preferidas(request,id_de_la_tienda): 
     tiendas = Tiendas.objects.get(pk=id_de_la_tienda)
     idusuario=tiendas.id_usuario 
     nombretienda=tiendas.nombre_tienda
      
     categoria=categorizar(idusuario,nombretienda)     
     var=tiendas.codigoapk  

     lafecha=datetime.datetime.now()


     conteo=Preferidas.objects.filter(id_comprador=request.user.username,tienda__id=id_de_la_tienda).count()

     if conteo<=0:
          a=Preferidas(id_comprador=request.user.username,tienda=tiendas,fecha_ingreso=lafecha)
          a.save()
     else:    
        Preferidas.objects.get(tienda__id=id_de_la_tienda).delete()     

     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def ver_las_preferidas(request):

       preferidas=Preferidas.objects.filter(id_comprador=request.user.username)     
       pk_tiendas=preferidas.values_list("tienda", flat=True)     
       tiendas=Tiendas.objects.filter(pk__in=pk_tiendas)

                              
       connection.close()                       
       return render(request,'catalogo.html',locals())   




@login_required
def evaluar(request,id_pedido_evaluado,nota_evaluacion):
      categoria=n_categorias()
      mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
      ciudad, t_usuario, n_usuarios, n_tiendas, n_productos,n_pedidos,n_mensajes=info_pagina(request) 

      pedido=Carro_de_compras.objects.get(pk=id_pedido_evaluado)
      
      comprador=pedido.id_comprador
      el_evaluador=t_usuario

     
      if el_evaluador=="EL_COMPRADOR":
          el_evaluado=pedido.producto.tienda.id_usuario              
      else:
          el_evaluado=comprador
        


      if nota_evaluacion=="SI":
            la_nota=2
      elif nota_evaluacion=="TALVES":
             la_nota=-1
      else:
             la_nota=-3
      
     

      try:     
            conteo=Evaluacion.objects.filter(id_evaluador=request.user.username,id_evaluado=el_evaluado).count()      
            if conteo==0:
                  evaluin=Evaluacion(id_evaluador=request.user.username,id_evaluado=el_evaluado,nota=la_nota)
                  evaluin.save()
            else:
                evaluacion=Evaluacion.objects.filter(id_evaluador=request.user.username,id_evaluado=el_evaluado).first()
                evaluacion.nota=la_nota
                evaluacion.save()  
     
      except:
            pass      


      nota_evaluado=0
      evaluacion=Evaluacion.objects.filter(id_evaluado=el_evaluado)
      for i in evaluacion:
          nota_evaluado=nota_evaluado+i.nota

  

      if nota_evaluado>10:
              nota_evaluado=10
      
      if nota_evaluado<0:
              nota_evaluado=0
      


      if el_evaluador=="EL_COMPRADOR":
            pedido.producto.tienda.nota_de_evaluacion= nota_evaluado 
            pedido.save()
                        
      else:

            
            comprador_evaluado=Usuarios.objects.get(id_usuario=el_evaluado)
            comprador_evaluado.nota_de_evaluacion= nota_evaluado 
            comprador_evaluado.save() 
           

      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def administrar_mis_categorias(request,id_de_la_tienda):            
            
            tiendas=Tiendas.objects.get(id=id_de_la_tienda) 
            categoria=categorizar(request.user.username,tiendas.nombre_tienda)

            visitas=tiendas.n_visitas

            tiendas.n_visitas+=1      
            tiendas.save()

            corazon=Preferidas.objects.filter(id_comprador=request.user.username,tienda__id=tiendas.id).count()
            if corazon>0:
                corazon="PREFERIDA"
            else:
                corazon="NO_PREFERIDA"
            
            var=tiendas.codigoapk    

            categorias_tienda=Categoria.objects.filter(id_usuario=request.user.username,tienda=tiendas.nombre_tienda)
           
            return render(request,'ver_categorias_de_mi_tienda.html',locals()) 

@login_required
def borrar_categoria_de_mi_tienda(request,acid,id_de_la_tienda):
        tiendas=Tiendas.objects.get(id=id_de_la_tienda) 
        categoria=categorizar(request.user.username,tiendas.nombre_tienda)

        visitas=tiendas.n_visitas

        tiendas.n_visitas+=1      
        tiendas.save()

        corazon=Preferidas.objects.filter(id_comprador=request.user.username,tienda__id=tiendas.id).count()
        if corazon>0:
                corazon="PREFERIDA"
        else:
                corazon="NO_PREFERIDA"
            
        var=tiendas.codigoapk

        Categoria.objects.get(id=acid).delete()
        categorias_tienda=Categoria.objects.filter(id_usuario=request.user.username,tienda=tiendas.nombre_tienda)
           
        return render(request,'ver_categorias_de_mi_tienda.html',locals()) 




@login_required
def editar_categoria_de_mi_tienda(request,acid,id_de_la_tienda): 
        
        tiendas=Tiendas.objects.get(id=id_de_la_tienda) 
        categoria=categorizar(request.user.username,tiendas.nombre_tienda)

        visitas=tiendas.n_visitas

        tiendas.n_visitas+=1      
        tiendas.save()

        corazon=Preferidas.objects.filter(id_comprador=request.user.username,tienda__id=tiendas.id).count()
        if corazon>0:
                corazon="PREFERIDA"
        else:
                corazon="NO_PREFERIDA"
            
        var=tiendas.codigoapk     
        
        
        f = Categoria.objects.get(pk=acid)           
       
        if request.method == 'POST':
            form = CategoriaForm(request.POST,request.FILES,instance=f)
       
            if form.is_valid():
                    form.save()
                    connection.close()
                    return render(request,'confirmar_tienda.html',locals())

        else:
            
            form = CategoriaForm(instance=f)   
        
        connection.close()
        return render(request,'editar_categorias_de_mi_tienda.html',locals())
    

@login_required        
def traspasar_tienda(request,id_de_la_tienda):
            tiendas=Tiendas.objects.get(id=id_de_la_tienda) 
            categoria=categorizar(request.user.username,tiendas.nombre_tienda)

            visitas=tiendas.n_visitas

            tiendas.n_visitas+=1      
            tiendas.save()

            corazon=Preferidas.objects.filter(id_comprador=request.user.username,tienda__id=tiendas.id).count()
            if corazon>0:
                corazon="PREFERIDA"
            else:
                corazon="NO_PREFERIDA"
            
            var=tiendas.codigoapk

             


            if request.POST:
                nuevo_id_usuario_tienda = request.POST.get('nombret')
                #guarda la palabra buscada siempre y cuando no exista EN EL REGISTRO DE BUSQUEDA
                nuevo_id=Usuarios.objects.get(id_usuario=nuevo_id_usuario_tienda)
                
                if nuevo_id.tipo_usuario=="EL_ADMINISTADOR":                  
                      tienda_traspasada=Tiendas.objects.get(id=id_de_la_tienda)
                      tienda_traspasada.id_usuario=nuevo_id_usuario_tienda
                      tienda_traspasada.save()

                      producto_traspasado=Productos.objects.filter(tienda__id=id_de_la_tienda)
                      
                      if producto_traspasado.count()>0:
                        
                            for i in producto_traspasado:
                                i.id_usuario=nuevo_id_usuario_tienda
                                i.save()


            connection.close()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    



   


