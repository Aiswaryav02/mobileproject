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
    





#     form_class=Productform
#     success_url=reverse_lazy('uhm')
#     def form_valid(self, form) :
#         form.instance.user=self.request.user
#         self.object=form.save()
#         messages.success(self.request,"purchased successfully")
#         return super().form_valid(form)

    # def get(self,request,*args,**kwargs):???
    #         form=PurchaseForm()
    #         return render(request,"purch.html",{'form':form})?//


    # def post(self,request,*args,**kwargs):
    #         form_data=PurchaseForm(request.POST)
    #         if form_data.is_valid():
    #             form_data.save()
    #             messages.success(request,"Purchased")
    #             return redirect('purch')
    #         else:
    #             messages.error(request,"failed")
    #             return redirect('prod')


    # def post(self,request,*args,**kwargs):
    #     purch=Purchase(product=productname,user=request.user,quantity=Products.price)
    #     purch.save()
    #     messages.success(request,"Purchased")
    #     return redirect('purch')
    

    
# class PurchaseView(CreateView):
#     # def get(self,req,*args,**kwargs):
#     #     user=req.user
#     #     return render(req,"home2.html",{'user_data':user})
#     template_name="purchases.html"
#     model=Purchase
#     form_class=PurchaseForm
#     success_url=reverse_lazy('purch')
#     def form_valid(self, form) :
#         form.instance.user=self.request.user
#         self.object=form.save()
#         messages.success(self.request,"purchased")
#         return super().form_valid(form)
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         blog=self.model.objects.all().order_by('-date')
#         context['product']=blog
#         prod=PurchaseForm()
#         context['product']=prod
#         context['product']=Purchase.objects.all()
#         return context


        
# class Orders(CreateView):?????
    # def get(self,req,*args,**kwargs):
    #     user=req.user
    #     return render(req,"home2.html",{'user_data':user})
    # template_name="myorders.html"
    # model=MyOrders
    # form_class=PurchaseForm
    # success_url=reverse_lazy('orders')
    # def form_valid(self, form) :
    #     form.instance.user1=self.request.user
    #     self.object=form.save()
    #     messages.success(self.request,"ordered succesfully")
    #     return super().form_valid(form)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     order=self.model.objects.all().order_by('-date')
    #     context['product']=order
    #     cmnt=PurchaseForm()
    #     context['product']=cmnt
    #     context['product']=MyOrders.objects.all()
    #     return context????/

        



# class Myorderview(View):
#         def get(self,request,*args,**kwargs):
#             order=MyOrders.objects.filter(user_id=self.request.user)
#             return render(request,"myorders.html",{'data':order})
           




# @method_decorator(signin_required,name="dispatch")
# class OrderCreateVIew(View):
#     def get(self,request,*args,**kwargs):
#         user=request.user
#         p_id=kwargs.get('id')
#         product=Products.objects.get(id=p_id)
#         MyOrders.objects.create(user=user,product=product)
#         messages.success(request,"ordered succesfully")
#         return redirect('uhm')
         
@method_decorator(signin_required,name="dispatch")
class Myorderview(TemplateView):
        template_name="myorders.html"
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            order=MyOrders.objects.filter(user_id=self.request.user)
            context['data']=order
            # context['cmnts']=CommentModel.objects.all()
            return context
# def feedback(request,*args,**kwargs):
# class FeedbackView(CreateView):
#     model = FeedbackModel
#     form_class=FeedbackForm
#     template_name="feedbach.html"
#     success_url=reverse_lazy('uhm')
#     def post(self,request,*args,**kwargs):
        
        # print("hi")
        # if request.method=='POST':
            # fb=request.POST.get('feedback')
            # user=request.user
            # f_id=kwargs.get('id')
            # prod=Products.objects.get(id=f_id)
            # FeedbackModel.objects.create(feedback=fb,user=user,product=prod)
            # messages.success(request,"fb added")
            # return redirect('hme')


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
    # def get(self,request,*args,**kwargs):
        

        # user=request.user
        # f_id=kwargs.get('id')
        # product=Products.objects.get(id=f_id)
        # FeedbackModel.objects.create(user=user,product=product,)
        # messages.success(request,"succesfully")
        # return redirect('myorder')
    
        # if request.method=='POST':
        #     fb=request.POST.get('feedback')
        #     user=request.user
        #     f_id=kwargs.get('id')
        #     product=Products.objects.get(id=f_id)
        #     FeedbackModel.objects.create(user=user,product=product)
        #     messages.success(request,"succesfully")
        #     return redirect('myorder')
        


# class AddproView(CreateView):
#     template_name='addproducts.html'
#     model=Products
#     form_class=Productform
#     success_url=reverse_lazy('editprod')
# def post(self,request,*args,**kwargs):
#         form_data=self.form_class(request.POST)
#         if form_data.is_valid(): 
#             messages.success(request, "Product added!!!")
#             return redirect('editprod')
#         else:
#             messages.error(request, "Failed") 
#             return render(request, "addproducts.html", {'form': form_data})