from django.contrib import admin
from imaging.models import *

class ImageAdmin(admin.ModelAdmin):
  exclude = ['ordering', 'content_type', 'object_id', 'content_object' ]

admin.site.register(Image, ImageAdmin)
