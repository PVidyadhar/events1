from django.urls import path
from . import views
urlpatterns=[
    path('',views.homepage,name='home'),
    path('adminlogin',views.adminlogin,name='admin'),
    path('clublogin',views.clublogin,name='clublog'),
    path('clubsignup',views.clubsignup,name='clubsign'),
    path('mainadmin',views.mainadmin,name='adminmain'),
    path('clubreg',views.clubreg,name='regclub'),
    path('after_registration',views.after_registration,name='after_reg'),
    path('after_clublogin',views.after_clublogin,name='after_clublogin'),
    path('create_event',views.create_event,name='create_event'),
    path('after_createevent',views.after_createevent,name='created_event'),
]