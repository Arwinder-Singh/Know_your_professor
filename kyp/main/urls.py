from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dept/<str:department>/',views.dept,name='dept'),
    path('team/',views.team,name='team'),
    path('contact/',views.contact,name='contact'),
    path('profile/',views.profile,name='profile'),

]
