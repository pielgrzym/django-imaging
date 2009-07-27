from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.functional import curry
from imaging.utils import create_thumb, extract_filename, remove_thumb
from django.db.models.signals import post_init
from settings import MEDIA_URL
from django.utils.safestring import mark_safe
# Create your models here.

DEFAULT_IMAGING_SETTINGS = {
'image_sizes' : [
  { 
  'name':'small_thumb', 
  'width': 120,
  'height': 120,
  'aspect': False, 
  'suffix': '_thb'
  },
  { 
  'name':'large_thumb', 
  'width': 200,
  'height': 200,
  'aspect': False, 
  'suffix': '_big_thb'
  }
  ],
# a subdirectory of your MEDIA_ROOT - must be created manually
'image_dir' : 'imaging_photos',
    }

try:
  from settings import IMAGING_SETTINGS
except:
  IMAGING_SETTINGS = DEFAULT_IMAGING_SETTINGS

# default square admin thumbnail appended to current settings
admin_thumb = { 
  'name':'admin_thumb', 
  'width': 200,
  'height': 200,
  'aspect': True, 
  'suffix': '_athb'
  }
 
IMAGING_SETTINGS['image_sizes'].append(admin_thumb)

class Image(models.Model):
  name = models.CharField(max_length=200)
  alt = models.CharField(max_length=200, null=True, blank=True)
  title = models.CharField(max_length=200, null=True, blank=True)
  image = models.ImageField(upload_to=IMAGING_SETTINGS['image_dir'])
  ordering = models.PositiveIntegerField(null=True, blank=True)
  content_type = models.ForeignKey(ContentType, null=True, blank=True)
  object_id = models.PositiveIntegerField(null=True, blank=True)
  content_object = generic.GenericForeignKey('content_type', 'object_id')

  class Meta:
    ordering = ('ordering', 'name')
    permissions = (
        ('upload_images', "Can upload using AJAX"),
        ('ajax_delete_images', "Can delete using AJAX"),
        )

  def __unicode__(self):
    return self.name

  def _get_preset_url(self, preset):
    if self.id:
      directory = '%s%s/' % (MEDIA_URL, IMAGING_SETTINGS['image_dir'])
      return directory+extract_filename(self.image.path)+preset['suffix']+".jpg"      

  def get_admin_list_thumbnail(self):
    thb_url = self.get_small_thumb_url()
    return mark_safe('<img src="'+thb_url+'" />')
  get_admin_list_thumbnail.allow_tags = True
 
  def save(self, force_insert=False, force_update=False):
    original_image = self.image
    for preset in IMAGING_SETTINGS['image_sizes']:
      create_thumb(self.image, preset['width'], preset['height'], preset['suffix'], preset['aspect'])
    super(Image, self).save()

  def delete(self):
    original_image = self.image
    #TODO: figoure out why it tries to delete thumbnails twice...
    try:
      for preset in IMAGING_SETTINGS['image_sizes']:
        remove_thumb(original_image, preset)
    except:
      pass
    super(Image, self).delete()
  
  def add_extra_methods(self):
    '''
    Adds methods to fetch thumbnail urls, for default preset for example:
    get_small_thumb_url
    '''
    for preset in IMAGING_SETTINGS['image_sizes']:
        setattr(self, 'get_%s_url' % preset['name'],
                curry(self._get_preset_url, preset=preset))
        

def add_methods(sender, instance, signal, *args, **kwargs):
    if hasattr(instance, 'add_extra_methods'):
        instance.add_extra_methods()

# connect the add_accessor_methods function to the post_init signal
post_init.connect(add_methods)
