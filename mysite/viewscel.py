#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic import View
from django import get_version
from django.http import HttpResponse

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


def app_cel():



	return render(request,'cel_principal.html',locals())  



          
