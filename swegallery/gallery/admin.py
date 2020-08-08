from django.contrib import admin
from gallery .models import Gallery,all_images,Contact
# Register your models here.


'''
class GalleryAdmin(admin.ModelAdmin):
    class Meta:
        model = Gallery
    list_display = ['id','event_name','admin_name']
    list_display_links = ['id','event_name']
    list_filter = ('admin_name'),
    search_fields = ('event_name','description','admin_name'),
    list_per_page = 20

admin.site.register(Gallery,GalleryAdmin)
'''


class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model= Contact

    list_display = ['id', 'name', 'subject']
    list_display_links = ['id', 'name']

admin.site.register(Contact,ContactAdmin)

class PostImageAdmin(admin.StackedInline):
    model = all_images
@admin.register(Gallery)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Gallery
@admin.register(all_images)
class PostImageAdmin(admin.ModelAdmin):
    pass