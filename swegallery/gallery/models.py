from django.db import models
from registration .models import User
# Create your models here.

class Gallery(models.Model):
    admin_name = models.ForeignKey(User,on_delete=models.CASCADE)
    event_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d')
    '''
    photo1 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photos2 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photos3 = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    photos4 = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    photos5 = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    photos6 = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    '''

    def __str__(self):
        return self.event_name
    class Meta:
        ordering = ('-list_date',)

class all_images(models.Model):
    gallery = models.ForeignKey(Gallery,default=None,on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='photos/%y/%m/%d')

    def __str__(self):
        return self.gallery.event_name



class Contact(models.Model):
    name=models.CharField(max_length=250,blank=False)
    email=models.EmailField()
    subject=models.CharField(max_length=500,blank=False)
    message=models.TextField()

    def __str__(self):
        return self.subject

class Event(models.Model):
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    name=models.CharField(max_length=250)
    date=models.DateField(auto_now_add=True)
    desc=models.TextField()

    def __str__(self):
        return self.name