from django.urls import path
from .views import UserHome,ProductView,OrderCreateVIew,Myorderview,FeedbackView
urlpatterns=[
    path('uhme/',UserHome.as_view(),name="uhm"),
    path('productview/',ProductView.as_view(),name="prodview"),
    # path('purch/<int:p_id>',PurchaseView.as_view(),name="purch"),
    # path('viewpurch/',Viewmypurch.as_view(),name="mypurch")
    # path('pur/<int:id>',purch,name="pur"),
    # path('orders/<int:b_id>',Orders.as_view(),name="orders"),
    # path('orderview/',OrdrView.as_view(),name="orderview"),
    path('myorder/',Myorderview.as_view(),name="myorder"),
    path('order/<int:id>',OrderCreateVIew.as_view(),name="order"),
    path('feedback/<int:id>',FeedbackView.as_view(),name="fb"),

    

    
]