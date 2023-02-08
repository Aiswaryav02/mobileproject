from django.urls import path
from .views import UserHome,ProductView,OrderCreateVIew,Myorderview,FeedbackView,Addcart,Viewcart,Placeorder,Buynnow
urlpatterns=[
    path('uhme/',UserHome.as_view(),name="uhm"),
    path('productview/',ProductView.as_view(),name="prodview"),
    path('addcart/<int:pid>',Addcart.as_view(),name="addcart"),
    path('myorder/',Myorderview.as_view(),name="myorder"),
    path('viewcart/',Viewcart.as_view(),name="viewcart"),
    path('order/<int:id>',OrderCreateVIew.as_view(),name="order"),
    path('feedback/<int:id>',FeedbackView.as_view(),name="fb"),
    path('plorder/<int:pid>',Placeorder.as_view(),name="plorder"),
    path('buynow/<int:id>',Buynnow.as_view(),name="buynow"),      
    

    
]