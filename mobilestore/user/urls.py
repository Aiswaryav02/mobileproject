from django.urls import path
from .views import ProfileView
urlpatterns=[
    path('prof/',ProfileView.as_view(),name="prof"),
    path('uhme/',ProfileView.as_view(),name="prof"),
]