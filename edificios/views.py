from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import EdificoForm
from .models import Edificios
from django_pdf.utileria import render_pdf

# Create your views here.

class EdificiosHomeView(View):
    def get(self,request,*args,**kwargs):
        edificios=Edificios.objects.filter(administrador=request.user)
        
        return render(request,'edificios/index.html',{'edificios':edificios})
    

class crear(View):
    #if request.method == "GET":
    def get(self,request,*args,**kwargs):
        form = EdificoForm()
        context = {
            'form':form
        }
        return render(request,'edificios/crear.html',context=context)
    def post(self,request,*args,**kwargs):
        form = EdificoForm(request.POST)
        if form.is_valid():
            edificio = form.save()
            form = EdificoForm()
        return redirect('/edificios')

def ToPDF(request,id):
    edificio=Edificios.objects.get(id=id)
    print(edificio)
    pdf=render_pdf("edificios/to_pdf.html",{"edificio":edificio})
    return HttpResponse(pdf, content_type="application/pdf")

