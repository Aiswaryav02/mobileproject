from django.urls import path
from .views import StoreHome ,AddproView,DeletePROD,ProduView,EditProd
urlpatterns=[
    path('shm/',StoreHome.as_view(),name="shm"),
    path('addpro/',AddproView.as_view(),name="addpro"),
    path('editprod/',ProduView.as_view(),name="editprod"),
    path('delprod/<int:did>',DeletePROD.as_view(),name="delprod"),
    path('edit2prod/<int:did>',EditProd.as_view(),name="edit2prod"),
]