from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dept/',views.dept,name='dept'),
    path('team/',views.team,name='team'),
    path('contact/',views.contact,name='contact'),
]
