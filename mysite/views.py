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
from templates import *

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/principal")


@login_required
def entrada_producto(request):                

     #!/usr/bin/python
     # -*- coding: latin-1 -*-
     import os, sys
     categoria=Categoria.objects.all().order_by("categoria") 
    
     if request.method == 'POST': # si el usuario est enviando el formulario con datos
            
                         
            if request.POST:

                  formProd=ProductosForm(request.POST,request.FILES)                   
                  
                  if formProd.is_valid():
                          productillo = formProd.save(commit=False)
                          # commit=False tells Django that "Don't send this to database yet.
                          # I have more things I want to do with it."
                          productillo.id_usuario = request.user.username # Set the user object here             
                                           
                          productillo.save() # Now you can send it to DB
                          formProd.save()  
                          
                          return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
                  
                  else:


                          formCateg=CategoriaForm(request.POST,request.FILES) 
                          if formCateg.is_valid() :                           

                                  categor = formCateg.save(commit=False)
                                  # commit=False tells Django that "Don't send this to database yet.
                                  # I have more things I want to do with it."
                                  categor.id_usuario = request.user.username # Set the user object here
                                  categor.save() # Now you can send it to DB
                                  formCateg.save() # Guardar los datos en la base de datos  print                             
                                 
                                          
     else:                        return render(request,'entrada_producto.html',locals())
                        
                          formProd=ProductosForm()
                          formCateg=CategoriaForm()
                         

     
     return render(request,'entrada_producto.html',locals())
        #return render_to_response('formulario.html', locals() ,context_instance=RequestContext(request))


@login_required
def entrada_mensaje(request,bandera): 
        categoria=Categoria.objects.all().order_by("categoria")           

        if request.method == 'POST': # si el usuario est enviando el formulario con datos
            
                    form = MensajeForm(request.POST)  

                    if form.is_valid():
                        mensajero = form.save(commit=False)
                        # commit=False tells Django that "Don't send this to database yet.
                        # I have more things I want to do with it."
                        mensajero.id_usuario = request.user.id # Set the user object here
                        mensajero.save() # Now you can send it to DB
                     

                        return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
       
        else:            
                        form = MensajeForm()


                        
        if bandera=="0": 
                  

                  mensajes_anteriores=Mensaje.objects.filter(id_usuario=request.user.id).order_by("-id")    
                  
        else:
                  
                  mensajes_anteriores=Mensaje.objects.all().order_by("-id") 
    
        

        return render_to_response('mensajes.html', locals() ,context_instance=RequestContext(request))



def entrada_usuario(request): 
        categoria=Categoria.objects.all().order_by("categoria")
       
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
                            return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
       
        else:            
                        

                         form=UsuariosForm()

       
        return render_to_response('formulario.html', locals() ,context_instance=RequestContext(request))
    
def editar_usuario(request,acid):    
        categoria=Categoria.objects.all().order_by("categoria")
        f = Usuarios.objects.get(id_usuario=acid)           
       
        if request.method == 'POST':
            form = UsuariosForm(request.POST,request.FILES,instance=f)
       
            if form.is_valid():
                    usu=form.save(commit=False)
                    usu.id_usuario = request.user.username
                    usu.clave = request.user.password
                    usu.save() # Guardar los datos en la base de datos 
                    return render_to_response('confirmar.html',locals(),context_instance=RequestContext(request))          
        
        else:
            
            form = UsuariosForm(instance=f)   
        

        return render_to_response('formulario.html', locals(),context_instance=RequestContext(request))



def listado_productos(request,ordenados): 

    categoria=Categoria.objects.all().order_by("categoria")        
    if ordenados=="recientes":
        productos=Productos.objects.filter(id_usuario=request.user.username).order_by("fecha_ingreso")
    elif ordenados=="antiguos": 
        productos=Productos.objects.filter(id_usuario=request.user.username).order_by("-fecha_ingreso") 
    elif ordenados=="menorp":
        productos=Productos.objects.filter(id_usuario=request.user.username).order_by("precio_A")
    
    elif ordenados=="mayorp":
        productos=Productos.objects.filter(id_usuario=request.user.username).order_by("-precio_A")     
    
    else:
        productos=Productos.objects.filter(id_usuario=request.user.username)    
    

    return render_to_response('catalogo.html', locals(),context_instance=RequestContext(request))

   
   

    
@login_required
def editar(request, acid):
    categoria=Categoria.objects.all().order_by("categoria")
    #if = Producto.objects.get(pk=acid)    
    ##message = Pedido.objects.get(pk=id)
    #if request.method == 'POST':
    #    form = ProductoForm(request.POST,instance=f)
    #    if form.is_valid():
    #        form.save() 
    #        return render_to_response('confirmar.html',locals(),context_instance=RequestContext(request))          
    #else:
    #    form = ProductoForm(instance=f)    
    #    
    return render_to_response('formulario.html',locals(),context_instance=RequestContext(request))


def mi_tienda(request,nombre):
  vendedor=Usuarios.objects.filter(id_usuario=nombre).first()

  productos=Productos.objects.filter(id_usuario=nombre)
  categorias=Categoria.objects.filter(id_usuario=nombre)


  
  #if vendedor.plan_tienda!="":
  return render_to_response('principal_tienda.html',locals(),context_instance=RequestContext(request))
  #else:
  #      return render_to_response('no_tienes_tienda.html',locals(),context_instance=RequestContext(request))



def ver_categorias(request,item):
  
  categoria=Categoria.objects.all().order_by("categoria")
  respuesta=request.POST.getlist('selec1')
  

  if item=="todas las categorias":
    productos=Productos.objects.all()
  else:
    #productos=Productos.objects.all()
    productos=Productos.objects.filter(categoria__categoria__contains=item)
    
   

  return render_to_response('catalogo.html',locals(),context_instance=RequestContext(request))

    

 


def busqueda(request):
     categoria=Categoria.objects.all().order_by("categoria")
     
     if request.POST:
        palabra = request.POST.get('nombre')
        #guarda la palabra buscada siempre y cuando no exista EN EL REGISTRO DE BUSQUEDA
        if Buscar.objects.filter(id_usuario=request.user.username,item_de_busqueda=palabra).count() <= 0:
            busqueda=Buscar(id_usuario=request.user.username,item_de_busqueda=palabra)
            busqueda.save()
            
        productos= Productos.objects.filter(Q(categoria__categoria__icontains=palabra) | Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra))
                   


         
        return render_to_response('catalogo.html',locals(),context_instance=RequestContext(request))


    
  
   

import datetime
#@login_required
def pagina_principal(request):
                        

                         categoria=Categoria.objects.all().order_by("categoria")

                         
                         #publicidad=Buscar.objects.filter(id_usuario=request.user.username)

                         #user=Usuarios.objects.filter(plan_publicidad="PRODUCTO")

                         #p=[]
                         #for i in user:                            
                         #   productos=Product.objects.filter(id_usuario=i.username)[0:4]
                         #   p.append(productos)

                         #nuevas_tiendas=Usuarios.objects.filter(plan_publicidad="TIENDA")[0:4] 
                         nuevas_tiendas=Usuarios.objects.exclude(plan_tienda__isnull=True).exclude(plan_tienda="").order_by("-fecha_ingreso")[0:4] 
                        
 
                         nuevos_productos=Productos.objects.all().order_by("-fecha_ingreso")[0:4]

                         usuario=Usuarios.objects.filter(id_usuario=request.user.username).first()

                         return render_to_response('principal.html', locals(),context_instance=RequestContext(request))



def catalogo(request, var):
  categoria=Categoria.objects.all().order_by("categoria")
  return render_to_response('catalogo.html', locals(),context_instance=RequestContext(request))

def informacion(request):
  categoria=Categoria.objects.all().order_by("categoria")
  return render_to_response('informacion.html', locals(),context_instance=RequestContext(request))


from datos_artetronica.cart import Cart

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

    print  "########"
    print  quantity, productos, precio 
    cart = Cart(request)
    cart.add(productos, precio, quantity)
    total=cart.summary()
    

    return render_to_response('carrito.html', locals(),context_instance=RequestContext(request))

@login_required
def remove_from_cart(request, product_id):
    categoria=Categoria.objects.all().order_by("categoria")
    product = Productos.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

@login_required
def get_cart(request):
    categoria=Categoria.objects.all().order_by("categoria")
    print "getcqr" 
    cart = Cart(request)
    cart.view()
    return render_to_response('carrito.html', locals(),context_instance=RequestContext(request))

@login_required
def pedido(request):   
    categoria=Categoria.objects.all().order_by("categoria") 
    cart = Cart(request)
    cart.view()    
    fecha= datetime.datetime.now()
    
    mensaje= str(fecha)+"  "+str(request.user.first_name) + "  "+str(request.user.last_name) +"  "+ str(request.user.id)+"  "+"\n"

    for item in cart:
        mensaje=mensaje+"  "+ str(item.productos)+ "  "+ str(item.unit_price)+ "  "+str(item.quantity)+"  "+ str(item.total_price)+"  "+"\n"

                                
    mensaje=mensaje+"\n" 
     
    sender =str(request.user.email)

    send_mail('Pedido ', mensaje,"artetronica@gmail.com",(sender,), fail_silently=False)
   
    
    return render_to_response('cotizacion.html', locals(),context_instance=RequestContext(request))
 
