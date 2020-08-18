
from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.login,name ='login'),
    path('',views.registration,name ='registration'),
    path('logout/',views.logout,name='logout'),
]
