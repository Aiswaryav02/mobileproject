from django.shortcuts import render
from django.views.generic import View,CreateView
from django.urls import reverse_lazy
# Create your views here.

    
class Uhome(CreateView):
    # def get(self,req,*args,**kwargs):
    #     user=req.user
    #     return render(req,"home2.html",{'user_data':user})
    template_name="home2.html"
    success_url=reverse_lazy('hme')