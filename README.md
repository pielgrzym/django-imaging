django-imaging v 1.0
====================

Ajax driven gallery field for django admin

[Screenshot] [1]

**After 2 years of slumber brought to life again**

Requirements
------------

* Django >= **1.2**
* Django Imagekit >= **1.0.0**
* Python PIL

Installation
------------

* Install imaging using easy_install or pip

```
    pip install django-imaging
```

* Put the contents of the media folder in your project's MEDIA_ROOT. Make sure the imaging_photos folder has 777 permissions.

* Add "imaging" to your INSTALLED_APPS tuple in settings.py

* Include imaging in your urls.py

```python
urlpatterns = patterns('',
(...)
(r'^imaging/', include('imaging.urls')),
(...)
)
```

Or ```include('myappname.imaging.urls')```

* Add ImagingField to desired model

```python
from imaging.fields import ImagingField

class Somemodel(models.Model):
    photos = ImagingField()
```

* Optionally add a related model field for easy image fetching

```python
from django.contrib.contenttypes import generic
from imaging.fields import ImagingField
from imaging.models import Image

class Somemodel(models.Model):
   photos = ImagingField()
   photos_set = generic.GenericRelation(Image)
```

* Optionally add a custom imaging config to your settings.py

```python
IMAGING_SETTINGS = {
    'image_dir' : 'funny_photos',
}
```

The images uploaded will be stored inside MEDIA_ROOT/funny_photos.

* Syncdb to create proper imaging tables.

Limitations
-----------

   1. Currently only one ImagingField? per model.
   2. Drag'n'drop doesn't work properly in Opera (jquery.ui.sortable related problem)
   3. No orphaned images management
   4. ManyToMany? relation with an Image not supported
   5. Need to add a GenericRelation? field manually, I can't figoure out how to autoadd it
   6. Exceptions not handled too well 

[1]: http://prymityw.pl/files/imaging.jpg "Imaging field screenshot"
