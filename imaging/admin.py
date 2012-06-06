from django.contrib import admin
from imaging.models import *

class ImageAdmin(admin.ModelAdmin):
  exclude = ['ordering', 'content_type']
  list_display = ('name', 'title')

admin.site.register(Image, ImageAdmin)
