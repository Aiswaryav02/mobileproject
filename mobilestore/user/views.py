from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View,CreateView,TemplateView
from django.urls import reverse_lazy
from .forms import UserForm,FeedbackForm
from django.utils.decorators import method_decorator
from django.contrib import messages
from account.models import User
from store.models import Products
from .models import MyOrders,FeedbackModel
from store.forms import Productform
# Create your views here.
# decorators
def signin_required(fn):
    def wrapper(req,*args,**kwargs):
        if req.user.is_authenticated:
            return fn(req,*args,*kwargs)
        else:
            return redirect('logi')
    return wrapper

@method_decorator(signin_required,name="dispatch")
class UserHome(CreateView):
    template_name="uhome.html"
    model=User
    form_class=UserForm
    success_url=reverse_lazy('hme')

@method_decorator(signin_required,name="dispatch")
class ProductView(View):
    model=Products
    form_class=Productform
    template_name='productview.html'
    success_url=reverse_lazy('prodview')
    def get(self,request):
        prod=Products.objects.all()
        return render(request,"prod.html",{'data':prod})
    

@method_decorator(signin_required,name="dispatch")
class OrderCreateVIew(View):
    def get(self,request,*args,**kwargs):
        user=request.user
        p_id=kwargs.get('id')
        product=Products.objects.get(id=p_id)
        MyOrders.objects.create(user=user,product=product)
        messages.success(request,"ordered succesfully")
        return redirect('uhm')
         
class Buynnow(View):
    def get(self,request,*args,**kwargs):
        return render(request,"buy.html")
    def post(self,request,*args,**kwargs):
        id=kwargs.get('id')
        product=Products.objects.get(id=id)
        quantity=request.POST.get("quantity")
        user=request.user
        MyOrders.objects.create(user=user,product=product,status="ordered",quantity=quantity)
        return redirect('myorder')


class Addcart(View):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get('pid')
        product=Products.objects.get(id=pid)
        user=request.user
        MyOrders.objects.create(user=user,product=product,status="cart")
        messages.success(request,"Added to Cart")
        return redirect('viewcart')

class Viewcart(View):
        def get(self,request,*args,**kwargs):
            user=request.user
            cart=MyOrders.objects.filter(user=user,status="cart")
            return render(request,"viewcart.html",{'data':cart})

class Placeorder(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pid')
        ord=MyOrders.objects.get(id=id)
        return render(request,"myord.html",{'data':ord})
    def post(self,request,*args,**kwargs):
        id=kwargs.get('pid')
        quantity=request.POST.get("quantity")
        ord=MyOrders.objects.get(id=id)
        ord.quantity=quantity
        ord.status="ordered"
        ord.save()
        return redirect('viewcart')
    
@method_decorator(signin_required,name="dispatch")
class Myorderview(TemplateView):
    def get(self,request,*args,**kwargs):
        user=request.user
        ord=MyOrders.objects.filter(status="ordered",user=user)
        return render(request,"myorders.html",{'data':ord})

class FeedbackView(CreateView):
    model = FeedbackModel
    form_class=FeedbackForm
    template_name="feedbach.html"
    success_url=reverse_lazy('uhm')
    def post(self,request,*args,**kwargs):
        form_data=self.form_class(request.POST)
        if form_data.is_valid(): 
            fb=form_data.cleaned_data.get('feedback')
            user=request.user
            f_id=kwargs.get('id')
            prod=Products.objects.get(id=f_id)
            FeedbackModel.objects.create(feedback=fb,user=user,product=prod)
            messages.success(request, "feedback added!!!")
            return redirect('uhm')
        else:
            messages.error(request, "Failed") 
            return render(request, "feedbach.html", {'form': form_data})
        

    