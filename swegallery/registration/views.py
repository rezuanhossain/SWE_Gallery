from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
# Create your views here.

def login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']

        count = User.objects.filter(email=email, password=password).count()

        if count > 0:
            request.session['logged']=True

            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Invalid Credentials!')
            return HttpResponseRedirect(reverse('login'))

    return render(request,'registration/login.html')

def registration(request):
    if request.POST:
        userid = request.POST['userid']
        email = request.POST['email']
        password = request.POST['password']
        batch = request.POST['batch']
        phone= request.POST['phone']

        if User.objects.filter(userid=userid).exists():
            messages.error(request, 'username already exists')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already Taken')
            else:
                if not '35-' and '@diu.edu.bd' in email:
                    messages.error((request, 'You are not from DIU SWE Department'))
                else:
                    obj = User(userid=userid, password=password, phone=phone, batch=batch,
                               email=email)
                    obj.save()
                    return HttpResponseRedirect(reverse('login'))
    return render (request,'registration/register.html')

def logout(request):
    del request.session['logged']
    return HttpResponseRedirect(reverse('login'))



