from django.contrib import admin
from gallery.models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Gallery, GalleryAdmin)
