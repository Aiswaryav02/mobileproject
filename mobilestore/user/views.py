from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View,CreateView,TemplateView
from django.urls import reverse_lazy
from .forms import UserForm
from django.contrib import messages
from account.models import User
from store.models import Products
from .models import MyOrders
from store.forms import Productform
# Create your views here.

class UserHome(CreateView):
    template_name="uhome.html"
    model=User
    form_class=UserForm
    success_url=reverse_lazy('hme')


class ProductView(View):
    model=Products
    form_class=Productform
    template_name='productview.html'
    success_url=reverse_lazy('prodview')
    def get(self,request):
        prod=Products.objects.all()
        return render(request,"prod.html",{'data':prod})
    
# class PurchaseView(View):
#     template_name="purchases.html"
#     def get_context_data(self, **kwargs):
#             context = super().get_context_data(**kwargs)
#             prod=Products.objects.filter(product=self.request.user)
#             context['data']=prod
#             context['purch']=Purchase.objects.all()
#             return context
    
#     model=Products




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


# def purch(request,*args,**kwargs):?????
#         print("hi")
#         if request.method=='POST':
#             cmnt=request.POST.get('product')
#             user=request.user
#             p_id=kwargs.get('id')
#             blog=Purchase.objects.get(id=p_id)
#             Purchase.objects.create(product=cmnt,user=user,blog=blog)
#             messages.success(request,"purchased added")
#             return redirect('purch')????


# def purchas(request,*args,**kwargs):
       
#         if request.method=='POST':
#             cmnt=request.POST.get('quantity')
#             user=request.user
#             b_id=kwargs.get('id')
#             blog=BlogModel.objects.get(id=b_id)
#             CommentModel.objects.create(comment=cmnt,user=user,blog=blog)
#             messages.success(request,"comment added")
#             return redirect('hme')
        
# class Viewmypurch(View):
#     def get(self,request):
#         dept=Purchase.objects.all()
#         return render(request,"purchases.html",{'data':dept})
# class Orders(TemplateView):
#         template_name="myorders.html"
#         def get_context_data(self, **kwargs):
#             context = super().get_context_data(**kwargs)
#             order=MyOrders.objects.filter(user1=self.request.user)
#             context['data']=order
#             context['product']=Products.objects.all()
#             return context
        
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

# def my_order(request,*args,**kwargs):
#         print("hi")
#         if request.method=='POST':
#             orde=request.POST.get('product')
#             user=request.user
#             b_id=kwargs.get('id')
#             blog=Products.objects.get(id=b_id)
#             MyOrders.objects.create(product=orde,user=user,model=blog)
#             messages.success(request,"ordered")
#             return redirect('orders')


# class OrdrView(CreateView): ?????
#     model=MyOrders
#     form_class=PurchaseForm
#     template_name="prod.html"
#     success_url=reverse_lazy('orders')????
    # def post(self,request,*args,**kwargs):
    #         form_data=PurchaseForm(request.POST)
    #         if form_data.is_valid():
    #             form_data.save()
    #             messages.success(request,"ordered")
    #             return redirect('myorder')
    #         else:
    #             messages.error(request,"failed")
    #             return redirect('prod')
            

        # def get(self,request,*args,**kwargs):
        #     prod=MyOrders.objects.filter(user_id=request.user.user_id)
        #     context['data']=prod
        #     context['cmnts']=Products.objects.all()
        #     return context
        



class Myorderview(TemplateView):
    template_name="myorders.html"
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            order=MyOrders.objects.filter(user=self.request.user).order_by('-date')
            context['data']=order
            return context


    # def get(self,request,*args,**kwargs):
    #     d_id=kwargs.get("did")
    #     prod=MyOrders.objects.get(id=d_id)
    #     form=PurchaseForm(instance=mng)
    #     return render(request,"myorders.html",{'data':prod})
# def getorder(self,request,*args,**kwargs):
#     product_id=kwargs.get('pid')
#     user=request.user
#     blog=MyOrders.objects.get(id=product_id)
#     blog.liked_by.add(user)
#     blog.save()
#     return redirect('hme')



# class OrderCreateVIew(View):
#     def get(self,request,*args,**kwargs):
#         user=request.user
#         p_id=kwargs.get('id')
#         product=Products.objects.get(id=p_id)
#         MyOrders.objects.create(user=user,product=product)
#         messages.success(request,"ordered succesfully")
#         return redirect('uhm')
         
#     def post(self,request,*args,**kwargs):
#         product_id=kwargs.get('pid')
#         MyOrders.objects.create(pid=product_id,user=request.user)
#         messages.success(request,"Purchased")
#         return redirect('uhm')
    
# def order(request,*args,**kwargs):
#     if request.method=='POST':
#             user=request.user
#             p_id=kwargs.get('id')
#             product=Products.objects.get(id=p_id)
#             MyOrders.objects.create(user=user,item=product)
#             messages.success(request,"ordered succesfully")
#             return redirect('uhm')
# class Myblog(TemplateView):
#         template_name="myblogs.html"
#         def get_context_data(self, **kwargs):
#             context = super().get_context_data(**kwargs)
#             blog=.objects.filter(author=self.request.user)
#             context['data']=blog
#             context['cmnts']=CommentModel.objects.all()
#             return context


# class FeedbackCreateView(CreateView):
#     model = FeedbackModel
#     form_class=FeedbackForm
#     template_name="feedback.html"
#     success_url=reverse_lazy('prodview')