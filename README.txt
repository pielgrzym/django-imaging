Quick start

1. Svn checkout

svn co http://django-imaging.googlecode.com/svn/trunk/ django-imaging

2. Put "imaging" folder into your python path (easiest way: put it in your django project directory)

3. Put the contents of the media folder in your project's MEDIA_ROOT

Make sure the imaging_photos folder has 777 permissions

4. Add "imaging" to your INSTALLED_APPS tuple in settings.py

5. Include imaging in your urls.py

urlpatterns = patterns('',
(...)
(r'^imaging/', include('imaging.urls')),
(...)
)

Or include('myappname.imaging.urls')

6. Add ImagingField? to desired model

from imaging.fields import ImagingField

class Somemodel(models.Model):
   photos = ImagingField()

7. Optionally add a related model field for easy image fetching

from django.contrib.contenttypes import generic
from imaging.fields import ImagingField
from imaging.models import Image

class Somemodel(models.Model):
   photos = ImagingField()
   photos_set = generic.GenericRelation(Image)

8. Optionally add a custom imaging config to your settings.py

IMAGING_SETTINGS = {
'image_sizes' : [
  { 
  'name':'my_custom_thumb', 
  'width': 190,
  'height': 150,
  'aspect': False, 
  'suffix': '_cus_thb'
  },
  ],
'image_dir' : 'funny_photos',
    }

Above example will make django-imaging create only one thumbnail size, without forcing the aspect ratio giving the thumbnail files suffix _cus_thb. The images uploaded will be stored inside MEDIA_ROOT/funny_photos. The image_sizes list can contain an unlimited thumbnail dictionaries. You can easily access a thumbnail of an image model by an auto-created method:

>>> image = Image.objects.get(pk=1)
>>> image.get_my_custom_thumb_url()

So basically the method name is built: get_+thumbnail_name+url()

9. Syncdb to create proper imaging tables.

Have fun :)
Limitations

   1. Currently only one ImagingField? per model.
   2. Drag'n'drop doesn't work properly in Opera (jquery.ui.sortable related problem)
   3. No orphaned images management
   4. ManyToMany? relation with an Image not supported
   5. Need to add a GenericRelation? field manually, I can't figoure out how to autoadd it
   6. Exeptions not handled too well 
