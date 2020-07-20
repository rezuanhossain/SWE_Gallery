from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from gallery.models import Gallery


def home(request):
    gallery_list = Gallery.objects.all()
    paginator = Paginator(gallery_list,3)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {
        'gallery_list':page_listings
    }
    return render(request,'gallery/photos.html',context)