from django.contrib import admin
from imaging.models import *

class ImageAdmin(admin.ModelAdmin):
  exclude = ['ordering', 'content_type', 'object_id', 'content_object' ]
  list_display = ('get_admin_list_thumbnail', 'name', 'title')

admin.site.register(Image, ImageAdmin)
