from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.temp.as_view()),
    path('work/',views.working.as_view(),name="work"),
    path('testing/',views.testing.as_view(),name="testing"),
    path('teste/',views.teste.as_view(),name="teste"),
    path('puter/<int:pk>/',views.puter.as_view(),name='putter'),
    path('pat/<int:pk>/',views.patcher.as_view(),name="patchc")
]
