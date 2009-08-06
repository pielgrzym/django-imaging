from django.contrib import admin
from imaging.models import *

class ImageAdmin(admin.ModelAdmin):
  exclude = ['ordering', 'content_type', 'object_id', 'content_object' ]
  list_display = ('name', 'title')

admin.site.register(Image, ImageAdmin)
