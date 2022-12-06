from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import DepartamentoForm
from .models import Departamentos

# Create your views here.

class DepartamentosHomeView(View):
    def get(self,request,*args,**kwargs):
        departamentos=Departamentos.objects.all()
        return render(request,'departamentos/index.html',{'departamentos':departamentos})
    
class crear(View):
    #if request.method == "GET":
    def get(self,request,*args,**kwargs):
        form = DepartamentoForm()
        context = {
            'form':form
        }
        return render(request,'departamentos/crear.html',context=context)
    
    def post(self,request,*args,**kwargs):
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            propietario = form.save()
            form = DepartamentoForm()
        return redirect('/departamentos')
