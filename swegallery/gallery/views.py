from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from gallery.models import Gallery,all_images,Contact,Event


def home(request):
    if request.session.has_key('logged'):
        gallery_list = Gallery.objects.all()
        paginator = Paginator(gallery_list,10)
        page = request.GET.get('page')
        page_listings = paginator.get_page(page)
        context = {
            'gallery_list':page_listings
        }
        return render(request,'gallery/home.html',context)
    else:
        return HttpResponseRedirect(reverse('login'))


def home_detail(request):
    gallery_list = Gallery.objects.all()
    context = {
        'gallery_list': gallery_list
    }

    return render(request, 'gallery/photos.html', context)

def about(request):
    return render(request,'gallery/about.html')

def contact(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        if Contact.objects.filter(email=email).exists():
            messages.error(request,'you already contact us')
        else:
            obj= Contact(name=name,email=email,subject=subject,message=message)
            obj.save()
            messages.success(request,'Successfully Send')
        return HttpResponseRedirect(reverse('contact'))



    return render(request, 'gallery/contact.html')

def event(request):
    events_info = Event.objects.all()
    paginator = Paginator(events_info, 2)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {
        'events_info':page_listings
    }
    return render(request, 'gallery/events.html',context)

def event_details(request,id):
    event_detials=Event.objects.get(id=id)
    context = {
        'event_detials': event_detials
    }
    return render(request, 'gallery/event.html', context)