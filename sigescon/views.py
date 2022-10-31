from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from edificios.models import Edificios

# Create your views here.
@login_required()

def HomeView(request):
    edificios=Edificios.objects.filter(administrador=request.user) 
    return render(request,'ingreso.html',{'edificios':edificios})

def ingreso(request,id):
    
    edificio=Edificios.objects.all()
    print(edificio)
    return render(request,'index.html',{'edificio':edificio})

def cerrarSesion(request):
    logout(request)
    return redirect('index')