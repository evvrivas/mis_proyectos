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


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/principal")


@login_required
def crear_producto(request,idusuario,nombretienda):               

     #!/usr/bin/python
     # -*- coding: latin-1 -*-
     import os, sys
     vector=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__contains=nombretienda))

     cat=[]
     for i in vector:
        cat.append(i)
     categoria= sorted(set(cat))
  
     tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first
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
     else:
           bandera=0

                 
     if bandera==1:
    

                 if request.method == 'POST': # si el usuario est enviando el formulario con datos
                        
                              form=ProductosForm(request.POST,request.FILES)                   
                              
                              if form.is_valid():
                                      productillo = form.save(commit=False)
                                      # commit=False tells Django that "Don't send this to database yet.
                                      # I have more things I want to do with it."
                                      productillo.id_usuario = request.user.username # Set the user object here             
                                                       
                                      productillo.save() # Now you can send it to DB
                                      form.save()  
                                      
                                      #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                                      return render(request,'confirmar.html',locals())     
                              else:


                                      formCateg=CategoriaForm(request.POST,request.FILES) 
                                      if formCateg.is_valid() :                           

                                              categor = formCateg.save(commit=False)
                                              # commit=False tells Django that "Don't send this to database yet.
                                              # I have more things I want to do with it."
                                              categor.id_usuario = request.user.username # Set the user object here
                                              categor.save() # Now you can send it to DB
                                              formCateg.save() # Guardar los datos en la base de datos  print  

                                              return render(request,'entrada_producto.html',locals())                           
                                             
                                                      
                 else:
                    form=ProductosForm()
                    formCateg=CategoriaForm()                         

                 
                 return render(request,'entrada_producto.html',locals())
     else:


          return render(request,'formulario_cambio_plan.html',locals())





def editar_producto(request,idusuario,nombretienda,acid):   
        vector=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__contains=nombretienda))

        cat=[]
        for i in vector:
            cat.append(i)
        categoria= sorted(set(cat))
  
        tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()
        
        f = Productos.objects.get(pk=acid)           
       
        if request.method == 'POST':
            
            form = ProductosForm(request.POST,request.FILES,instance=f)
       
            if form.is_valid():
                    form.save() 
                    return render(request,'confirmar.html',locals())             
            
            else:

                          formCateg=CategoriaForm(request.POST,request.FILES) 
                          if formCateg.is_valid() :                           

                                  categor = formCateg.save(commit=False)
                                  # commit=False tells Django that "Don't send this to database yet.
                                  # I have more things I want to do with it."
                                  categor.id_usuario = request.user.username # Set the user object here
                                  categor.save() # Now you can send it to DB
                                  formCateg.save() # Guardar los datos en la base de datos  print  

                                  return render(request,'entrada_producto.html',locals())  
        else:
            
            form = UsuariosForm(instance=f)
            formCateg=CategoriaForm()

        

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
                     

                        #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                        return render(request,'confirmar.html',locals())   
        else:            
                        form = MensajesForm()


                        
        if bandera=="0": 
                  

                  mensajes_anteriores=Mensajes.objects.filter(id_usuario=request.user.id).order_by("-id")    
                  
        else:
                  
                  mensajes_anteriores=Mensajes.objects.all().order_by("-id") 
    
        
        return render(request,'mensajes.html',locals())   
        #return render_to_response('mensajes.html', locals() ,context_instance=RequestContext(request))



def crear_usuario(request): 
        #!/usr/bin/python
        # -*- coding: latin-1 -*-
        categoria=Categoria.objects.all().order_by("categoria")
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
                            sender =str("artetronica@gmail.com")
                            send_mail('Nuevo usuario ', mensaje,"evvrivas@gmail.com",(sender,), fail_silently=False) 
                                                  
                            #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                            return render(request,'confirmar_usuario.html',locals())   
                   
                

        else:            
                         
                         form=UsuariosForm()
                         
        return render(request,'formulario_editar_usuario.html',locals()) 



        

def editar_usuario(request,idusuario,nombretienda,acid):   
       categoria=Categoria.objects.all().order_by("categoria")
       f = Usuarios.objects.get(pk=acid)           
       
       if request.method == 'POST':
            
            form = UsuariosForm(request.POST,request.FILES,instance=f)
       
            if form.is_valid():
                    usu=form.save(commit=False)
                    usu.id_usuario = request.user.username
                    usu.clave = request.user.password
                    usu.save() # Guardar los datos en la base de datos 
                    #return render_to_response('confirmar.html',locals(),context_instance=RequestContext(request))
                    fecha= datetime.datetime.now()
                    mensaje= str(fecha)+"  "+str(whatsapp) + "Acaba de registrarse "+"\n"
                    sender =str("artetronica@gmail.com")
                    send_mail('Editaron datos ', mensaje,"evvrivas@gmail.com",(sender,), fail_silently=False) 
                           

                    return render(request,'confirmar.html',locals())             
            
       else:
            
            form = UsuariosForm(instance=f)
            

        

       #return render_to_response('formulario.html', locals(),context_instance=RequestContext(request))
       return render(request,'formulario_editar_usuario.html',locals())   

@login_required
def crear_tienda(request):                

     #!/usr/bin/python
     # -*- coding: latin-1 -*-
     import os, sys
     categoria=Categoria.objects.all().order_by("categoria") 
    
     if request.method == 'POST': # si el usuario est enviando el formulario con datos
            
                         
            if request.POST:

                  form=TiendasForm(request.POST,request.FILES)                   
                  
                  if form.is_valid():
                          tiendecilla = form.save(commit=False)
                          # commit=False tells Django that "Don't send this to database yet.
                          # I have more things I want to do with it."
                          tiendecilla.id_usuario = request.user.username # Set the user object here             
                                           
                          tiendecilla.save() # Now you can send it to DB
                          form.save()  
                          
                          #return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                          return render(request,'confirmar.html',locals())     
                  else:


                          formCateg=CategoriaForm(request.POST,request.FILES) 
                          if formCateg.is_valid() :                           

                                  categor = formCateg.save(commit=False)
                                  # commit=False tells Django that "Don't send this to database yet.
                                  # I have more things I want to do with it."
                                  categor.id_usuario = request.user.username # Set the user object here
                                  categor.save() # Now you can send it to DB
                                  formCateg.save() # Guardar los datos en la base de datos  print  

                                  return render(request,'formulario_ingreso.html',locals())                           
                                 
                                          
     else:
        form=TiendasForm()
        formCateg=CategoriaForm()
                         

     
     return render(request,'formulario_ingreso.html',locals())
        #return render_to_response('formulario.html', locals() ,context_instance=RequestContext(request))

def editar_tienda(request,acid):   
        categoria=Categoria.objects.all().order_by("categoria")
        
        f = Tiendas.objects.get(pk=acid)           
       
        if request.method == 'POST':
            
            form = TiendasForm(request.POST,request.FILES,instance=f)
       
            if form.is_valid():
                    form.save() 
                    return render(request,'confirmar.html',locals())             
            
            else:

                          formCateg=CategoriaForm(request.POST,request.FILES) 
                          if formCateg.is_valid() :                           

                                  categor = formCateg.save(commit=False)
                                  # commit=False tells Django that "Don't send this to database yet.
                                  # I have more things I want to do with it."
                                  categor.id_usuario = request.user.username # Set the user object here
                                  categor.save() # Now you can send it to DB
                                  formCateg.save() # Guardar los datos en la base de datos  print  

                                  return render(request,'formulario_ingreso.html',locals())  
        else:
            
            form = TiendasForm(instance=f)
            formCateg=CategoriaForm()

        

        #return render_to_response('formulario.html', locals(),context_instance=RequestContext(request))
        return render(request,'formulario_ingreso.html',locals())   



def mi_tienda(request,usuario,nombretienda):
    
    vector=Productos.objects.filter(Q(id_usuario=usuario) & Q(tienda__nombre_tienda__contains=nombretienda))

    cat=[]
    for i in vector:
        cat.append(i)
    categoria= sorted(set(cat))
    usuario=Usuarios.objects.filter(id_usuario=request.user.username).first() 

    var=usuario.codigoapk
    tiendas=Tiendas.objects.filter(id_usuario=usuario,nombre_tienda=nombretienda).first() 
     
    productos=Productos.objects.filter(Q(id_usuario=usuario) & Q(tienda__nombre_tienda__contains=nombretienda))

    
    return render(request,'principal_tienda.html',locals())   
 
def mis_tiendas(request,idusuario):
  categoria=Categoria.objects.all().order_by("categoria")
  
  tiendas=Tiendas.objects.filter(id_usuario=idusuario)
  return render(request,'catalogo.html',locals())   

#def mis_productos(request,nombre): 
   # productos=Productos.objects.filter(id_usuario=nombre) 
  
  
 # return render(request,'principal_tienda.html',locals())   


def ver_categorias(request,item):
  
  categoria=Categoria.objects.all().order_by("categoria")
  
  

  if item=="xproductox":
    productos=Productos.objects.all()
  elif item=="xtiendax":
    tiendas=Tiendas.objects.all()
   
  else:  
    tiendas=Tiendas.objects.filter(categoria__categoria__contains=item)  
    productos=Productos.objects.filter(categoria__categoria__contains=item)    
    
  



  #return render_to_response('catalogo.html',locals(),context_instance=RequestContext(request))
  return render(request,'catalogo.html',locals())   

    
def ver_mis_categorias(request,idusuario,nombretienda,item):
  
  vector=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__contains=nombretienda))

  cat=[]
  for i in vector:
      cat.append(i)
  categoria= sorted(set(cat))
  
  tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()

  if item=="todas las categorias":    
    productos=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__contains=nombretienda)) 

    
  else:      
    productos=Productos.objects.filter(Q(categoria__categoria__contains=item) & Q(tienda__nombre_tienda__contains=nombretienda),Q(categoria=item)) 
   
   
  
  #return render_to_response('catalogo.html',locals(),context_instance=RequestContext(request))
  return render(request,'catalogo_tienda.html',locals())   
 
def busqueda_tienda(request,idusuario,nombretienda):
     
     vector=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__contains=nombretienda))

     cat=[]
     for i in vector:
          cat.append(i)
     categoria= sorted(set(cat))
     
     if request.POST:
        palabra = request.POST.get('nombre')
        #guarda la palabra buscada siempre y cuando no exista EN EL REGISTRO DE BUSQUEDA
        if Buscar.objects.filter(id_usuario=request.user.username,item_de_busqueda=palabra).count() <= 0:
            busqueda=Buscar(id_usuario=request.user.username,item_de_busqueda=palabra)
            busqueda.save()
        
        tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()
        productos= Productos.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra) & Q(tienda__nombre_tienda__contains=nombretienda))
        return render(request,'catalogo_tienda.html',locals()) 

def busqueda(request):
     categoria=Categoria.objects.all().order_by("categoria")
     
     if request.POST:
        palabra = request.POST.get('nombre')
        #guarda la palabra buscada siempre y cuando no exista EN EL REGISTRO DE BUSQUEDA
        if Buscar.objects.filter(id_usuario=request.user.username,item_de_busqueda=palabra).count() <= 0:
            busqueda=Buscar(id_usuario=request.user.username,item_de_busqueda=palabra)
            busqueda.save()



        productos= Productos.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra))
        tiendas= Tiendas.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre_tienda__icontains=palabra) | Q(descripcion__icontains=palabra))
     return render(request,'catalogo.html',locals())   
                  
         
        
     


    
  
   

import datetime
#@login_required
def pagina_principal(request):
                        

                         categoria=Categoria.objects.all().order_by("categoria")                         
                         
                         nuevas_tiendas=Tiendas.objects.all().order_by("-fecha_ingreso")[0:6]
                         
                         nuevos_productos=Productos.objects.all().order_by("-fecha_ingreso")[0:6]
                                            
                         return render(request,'principal.html',locals())   



def catalogo(request, var):
  categoria=Categoria.objects.all().order_by("categoria")

  #return render_to_response('catalogo.html', locals(),context_instance=RequestContext(request))
  return render(request,'catalogo.html',locals())   

def informacion(request):
  categoria=Categoria.objects.all().order_by("categoria")
  #return render_to_response('informacion.html', locals(),context_instance=RequestContext(request))
  return render(request,'informacion.html',locals())   


from mysite.datos_artetronica.cart import Cart

@login_required
def add_to_cart(request, product_id): 

    categoria=Categoria.objects.all().order_by("categoria")
    quantity= request.POST["cant"]
    product = Productos.objects.get(id=product_id)   

    if quantity==1:
        precio=productos.precio_A
    elif quantity>=2 and quantity <=5:
        precio=productos.precio_B
    elif quantity>=6:
        precio=productos.precio_C
    else :
        precio=productos.precio_A

   
    
    cart = Cart(request)
    cart.add(productos, precio, quantity)
    total=cart.summary()
    

    #return render_to_response('carrito.html', locals(),context_instance=RequestContext(request))
    return render(request,'carrito.html',locals())   

@login_required
def remove_from_cart(request, product_id):
    categoria=Categoria.objects.all().order_by("categoria")
    product = Productos.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

@login_required
def get_cart(request):
    categoria=Categoria.objects.all().order_by("categoria")
    
    cart = Cart(request)
    cart.view()
    #return render_to_response('carrito.html', locals(),context_instance=RequestContext(request))
    return render(request,'carrito.html',locals())   


@login_required
def cambiar_estado_pedido(request,idusuario,nombretienda,id_del_pedido):  

                        vector=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__contains=nombretienda))
                        cat=[]
                        for i in vector:
                           cat.append(i)
                        categoria= sorted(set(cat))

                        tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()                  

                        ped = Pedidos.objects.get(pk=id_del_pedido)
                                                                       
                        if ped.estado2=="ENCARGADO":
                             ped.estado2="PRODUCCION"
                        
                        elif ped.estado2=="PRODUCCION":
                              ped.estado2="EMPACADO"
                        
                        elif ped.estado2=="EMPACADO":
                              ped.estado2="ENTREGADO"

                        elif ped.estado2=="ENTREGADO":
                              ped.estado2="ENCARGADO"
 
                        else:
                          pass 
                       
                        ped.save() # Guardar los datos en la base de datos 
                        #bandera=ped.estado_del_pedido 
                        #pedidos=Pedido.objects.filter(estado_del_pedido=bandera) 
                        i=ped
                        return render(request,'catalogo_pedidos.html',locals())

@login_required
def editar_pedido(request,idusuario,nombretienda,acid): 
        vector=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__contains=nombretienda))
        cat=[]
        for i in vector:
            cat.append(i)
        categoria= sorted(set(cat))

        tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()   
        
        f = Pedidos.objects.get(pk=acid)           
       
        if request.method == 'POST':
            form = PedidosForm(request.POST,request.FILES,instance=f)
       
            if form.is_valid():
                    ped=form.save(commit=False)
                    ped.id_usuario =  request.user.username
                    ped.save() # Guardar los datos en la base de datos 
                    return render(request,'confirmar_tienda.html',locals())

        else:
            
            form = PedidosForm(instance=f)   
        

        return render(request,'pedido.html',locals())


@login_required
def hacer_pedido(request,idusuario,nombretienda): 
        vector=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__contains=nombretienda))
        cat=[]
        for i in vector:
            cat.append(i)
        categoria= sorted(set(cat)) 
        
        tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()


        if request.method == 'POST': # si el usuario est enviando el formulario con datos
            
                    form = PedidosForm(request.POST,request.FILES)   
                    if form.is_valid():

                        ped=form.save(commit=False)
                        ped.id_usuario = request.user.username
                        ped.save() # Guardar los datos en la base de datos 
                        
                        return render(request,'confirmar_tienda.html',locals())
        else:            
                       
                        form = PedidosForm()                

        
        return render(request,'pedido.html',locals())

     
     
        #return render_to_response('formulario.html', locals() ,context_instance=RequestContext(request))
@login_required
def listado_pedido(request,idusuario,nombretienda,bandera): 

    vector=Productos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda__contains=nombretienda))
    cat=[]
    for i in vector:
            cat.append(i)
    categoria= sorted(set(cat))
     
    tiendas=Tiendas.objects.filter(id_usuario=idusuario,nombre_tienda=nombretienda).first()

   
    if bandera=="TODOS":
        pedidos= Pedidos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda=nombretienda)).order_by("fecha_de_entrega")
    
    else:
                   
        pedidos= Pedidos.objects.filter(Q(id_usuario=idusuario) & Q(tienda__nombre_tienda=nombretienda) & Q(estado=bandera)).order_by( "fecha_de_entrega")
     
    return render(request,'catalogo_pedidos.html',locals())
        


