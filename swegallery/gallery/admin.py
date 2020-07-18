from django.contrib import admin
from gallery .models import Gallery
# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    class Meta:
        model = Gallery
    list_display = ['id','event_name','admin_name']
    list_display_links = ['id','event_name']
    list_filter = ('admin_name'),
    search_fields = ('event_name','description','admin_name'),
    list_per_page = 20

admin.site.register(Gallery,GalleryAdmin)