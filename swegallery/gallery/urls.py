
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('photos/',views.home_detail,name ='photos'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('event/',views.event,name='event'),
    path('<int:id>',views.event_details,name='event_detials'),
]