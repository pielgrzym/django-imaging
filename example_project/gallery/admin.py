from django.contrib import admin
from gallery.models import Gallery, SchoolClass

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Gallery, GalleryAdmin)

class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(SchoolClass, SchoolClassAdmin)
