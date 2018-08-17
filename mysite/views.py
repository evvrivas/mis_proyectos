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


   
def logout(request):
    auth.logout(request)
    
    return HttpResponseRedirect("/")



def info_usuario(request):

    usuario=Usuarios.objects.filter(id_usuario=request.user.username).firrst()
    cantidad_tiendas=Tiendas.objects.filter(id_usuario=request.user.username).count()    
    tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
    
    connection.close()

    return cantidad_usuarios, cantidad_tiendas, cantidad_productos


def info_pagina():
    cantidad_usuarios=Usuarios.objects.all().count()
    cantidad_tiendas=Tiendas.objects.all().count()
    cantidad_productos=Productos.objects.all().count()
    connection.close()
    return cantidad_usuarios, cantidad_tiendas, cantidad_productos



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
            
    connection.close()       
    return  tiendas,productos


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
        

@login_required

def crear_mensaje(request,bandera): 
        categoria=Categoria.objects.all().order_by("categoria")           

        if request.method == 'POST': # si el usuario est enviando el formulario con datos
            
                    form = MensajesForm(request.POST)  

                    if form.is_valid():
                        mensajero = form.save(commit=False)
                        # commit=False tells Django that "Don't send this to database yet.
                        # I have more things I want to do with it."
                        mensajero.id_usuario = request.user.id # Set the user object here
                        mensajero.save() # Now you can send it to DB
                     
                        connection.close()
                        #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                        return render(request,'confirmar.html',locals())   
        else:            
                        form = MensajesForm()


                        
        if bandera=="0": 
                  

                  mensajes_anteriores=Mensajes.objects.filter(id_usuario=request.user.id).order_by("-id")    
                  
        else:
                  
                  mensajes_anteriores=Mensajes.objects.all().order_by("-id") 
    
        connection.close()
        return render(request,'mensajes.html',locals())   
        #return render_to_response('mensajes.html', locals() ,context_instance=RequestContext(request))


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
        
        n_usuarios, n_tiendas, n_productos=info_pagina()
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
       n_usuarios, n_tiendas, n_productos=info_pagina()
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
     n_usuarios, n_tiendas, n_productos=info_pagina()
     mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username) 
    
     if request.method == 'POST': # si el usuario est enviando el formulario con datos
            form=TiendasForm(request.POST,request.FILES)                   
                  
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
        form=TiendasForm()
                                

     connection.close() 
     return render(request,'formulario_ingreso.html',locals())
        #return render_to_response('formulario.html', locals() ,context_instance=RequestContext(request))

def editar_tienda(request,acid):   
        categoria=n_categorias()
        n_usuarios, n_tiendas, n_productos=info_pagina()
        mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
        
        f = Tiendas.objects.get(pk=acid)           
       
        if request.method == 'POST':
            
            form = TiendasForm(request.POST,request.FILES,instance=f)
       
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
            
            form = TiendasForm(instance=f)
            

        
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
  n_usuarios, n_tiendas, n_productos=info_pagina()
  mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
  
  tiendas=Tiendas.objects.filter(id_usuario=idusuario)
  connection.close()
  return render(request,'catalogo.html',locals())   




#def mis_productos(request,nombre): 
   # productos=Productos.objects.filter(id_usuario=nombre) 
  
  
 # return render(request,'principal_tienda.html',locals())   


def ver_categorias(request,item):
  
  categoria=n_categorias()
  n_usuarios, n_tiendas, n_productos=info_pagina()
  mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
  
  

  if item=="xproductox":
    productos=Productos.objects.all()
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
     n_usuarios, n_tiendas, n_productos=info_pagina()
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
     connection.close()
     return render(request,'catalogo.html',locals())   
                  
   

import datetime
#@login_required
def pagina_principal(request):   


                         n_usuarios, n_tiendas, n_productos=info_pagina()
                         categoria=n_categorias()
                         mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username) 
                         configurar=Configuracion_sistema.objects.all().first()
                         
                         configurar.n_visitas+=1         
                         configurar.save()

                         
                         try:
                             tiendas,productos=publicida_inteligencia(request)
                         except:
                             pass
                         
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

                         
                         

                         connection.close()                    
                         return render(request,'principal.html',locals())   



def catalogo(request, var):
  categoria=n_categorias()
  n_usuarios, n_tiendas, n_productos=info_pagina()
  mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)

  #return render_to_response('catalogo.html', locals(),context_instance=RequestContext(request))
  connection.close()
  return render(request,'catalogo.html',locals())   

def informacion(request):
  categoria=n_categorias()
  n_usuarios, n_tiendas, n_productos=info_pagina()
  mis_tiendas=Tiendas.objects.filter(id_usuario=request.user.username)
  #return render_to_response('informacion.html', locals(),context_instance=RequestContext(request))
  connection.close()
  return render(request,'informacion.html',locals())   

def informacion_vendedor(request,idusuario):
      categoria=n_categorias()
      n_usuarios, n_tiendas, n_productos=info_pagina()
     

      usuario=Usuarios.objects.filter(id_usuario=idusuario).first()
      cantidad_tiendas=Tiendas.objects.filter(id_usuario=idusuario).count()    
      tiendas=Tiendas.objects.filter(id_usuario=idusuario)
      connection.close()
      
      return render(request,'informacion_vendedor.html',locals())   



from mysite.datos_artetronica.cart import Cart

@login_required

def add_to_cart(request,product_id,idusuario,nombretienda):    
    
    categoria=n_categorias()
    n_usuarios, n_tiendas, n_productos=info_pagina()
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
    n_usuarios, n_tiendas, n_productos=info_pagina()
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


def comentario_tienda(request,idusuario,nombretienda,producto):
   
    categoria=categorizar(idusuario,nombretienda)    
    
    tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first() 
    
    
    if request.POST:

        coment = request.POST.get('comentario')
        
        
        if request.user.username:
               ncontacto=request.user.username
               lafecha=datetime.datetime.now()
               mensaje=Mensajes(id_usuario=tiendas.id_usuario,contacto=ncontacto,pregunta=coment,nombre_producto=producto,estado="NO_ATENDIDO",fecha=lafecha)
               mensaje.save()
           
        else: 
            ncontacto = request.POST.get('telefono')
            if ncontacto=="":
              pass
            else:
               lafecha=datetime.datetime.now()               
               mensaje=Mensajes(id_usuario=tiendas.id_usuario,contacto=ncontacto,pregunta=coment,nombre_producto=producto,estado="NO_ATENDIDO",fecha=lafecha)
               mensaje.save()
        
    connection.close()    
    return render(request,'confirmar_tienda.html',locals()) 



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



