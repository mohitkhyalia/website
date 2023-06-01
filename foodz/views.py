from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from .models import main_ad,option,fb,foodlist
# Create your views here.

def home(request):
    rvu = fb.objects.all()
    con = main_ad.objects.all()
    tbl = option.objects.all()
    
    return render(request,'index.html',{'con':con,'tbl':tbl,'rvu':rvu})

def review(request):
    
    return render(request,'staf.html')

def save(request):
    if request.method=='POST':
        name = request.POST['name']
        msg = request.POST['msg']
        email= request.POST['email']
        info=fb(name=name,msg=msg,mail=email)
        info.save()
    
    return redirect(home)

def br(request):
    other = foodlist.objects.all()
    mad= main_ad.objects.all()
    return render(request,'food.html',{'other':other,'mad':mad})

def roti(request):
    other = foodlist.objects.all()
    mad= foodlist.objects.filter(name='roti')
    return render(request,'food.html',{'other':other,'mad':mad})

def puri(request):
    other = foodlist.objects.all()
    mad= foodlist.objects.filter(name='puri')
    return render(request,'food.html',{'other':other,'mad':mad})

def ice(request):
    other = foodlist.objects.all()
    mad= foodlist.objects.filter(name='ice')
    return render(request,'food.html',{'other':other,'mad':mad})

def pav(request):
    other = foodlist.objects.all()
    mad= foodlist.objects.filter(name='pav')
    return render(request,'food.html',{'other':other,'mad':mad})