from django.urls import path
from .views import*

urlpatterns = [
    path('reg/',UserRegView.as_view(),name='reg'),
    path('logi/',LoginView.as_view(),name='logi'),
    path('logout/',SignOut.as_view(),name='logout'),
  
    ]
