from django.shortcuts import render
from django.http import HttpResponse
import requests
def homepage(request):
    data="club login"
    context={'data':data}
    return render(request,'index.html',context)
def adminlogin(request):
    data="Admin Login"
    context={'data':data}
    return render(request,'adminlogin.html',context)
def clublogin(request):
    data="club Login"
    context={'data':data}
    return render(request,'clublogin.html',context)
def clubsignup(request):
    data="Club Signup"
    context={'data':data}
    return render(request,'clubsignup.html',context)
def mainadmin(request):
    return render(request,'mainadminpage.html')
def clubreg(request):
    data="club Registration"
    context={'data':data}
    return render(request,'clubregister.html',context)
def after_registration(request):
    return render(request,'thanks.html')
def after_clublogin(request):
    return render(request,'mainclublogin.html')
def create_event(request):
    return render(request,'create_event.html')
def after_createevent(request):
    return render(request,'event_created.html')

