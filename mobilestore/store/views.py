from django.shortcuts import render,redirect
from django.views.generic import View,CreateView
from django.urls import reverse_lazy
from .forms import StoreForm,Productform
from .models import Products
from account.models import User
from django.contrib import messages
from django.utils.decorators import method_decorator
# Create your views here.
def signin_required(fn):
    def wrapper(req,*args,**kwargs):
        if req.user.is_authenticated:
            return fn(req,*args,*kwargs)
        else:
            return redirect('logi')
    return wrapper


@method_decorator(signin_required,name="dispatch")
class StoreHome(CreateView):
    template_name="storehome.html"
    model=User
    form_class=StoreForm
    success_url=reverse_lazy('hme')

@method_decorator(signin_required,name="dispatch")
class AddproView(CreateView):
    template_name='addproducts.html'
    model=Products
    form_class=Productform
    success_url=reverse_lazy('editprod')
def post(self,request,*args,**kwargs):
        form_data=self.form_class(request.POST)
        if form_data.is_valid(): 
            messages.success(request, "Product added!!!")
            return redirect('editprod')
        else:
            messages.error(request, "Failed") 
            return render(request, "addproducts.html", {'form': form_data})
        


@method_decorator(signin_required,name="dispatch")      
class ProduView(View):

    def get(self,request):
        prod=Products.objects.all()
        return render(request,"editprod.html",{'data':prod})


class DeletePROD(View):
    def get(self,request,*args,**kwargs):
        did=kwargs.get("did")
        item=Products.objects.get(id=did)
        item.delete()
        return redirect('editprod')
    
 
class EditProd(View):
    def get(self,request,*args,**kwargs):
        d_id=kwargs.get("did")
        item=Products.objects.get(id=d_id)
        form=Productform(instance=item)
        return render(request,"edit2prod.html",{'form':form})
    def post(self,request,*args,**kwargs):
        d_id=kwargs.get("did")
        item=Products.objects.get(id=d_id)
        form_data=Productform(request.POST,files=request.FILES,instance=item)
        if form_data.is_valid():
            form_data.save()
            return redirect('editprod')
        else:
            return redirect('addpro') 