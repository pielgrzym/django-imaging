from django.db import models
from django import forms
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save
#from django.forms import widgets

from imaging.forms import GalleryChoiceField
from imaging.legacy.fields import ImagingField

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([
        (
            [ImagingField], # Class(es) these apply to
            [],                 # Positional arguments (not used)
            {},                     # Keyword argument
        ),
    ], ["^imaging\.fields\.ImagingField"])
except ImportError:
    pass

class GalleryField(models.ManyToManyField):
    def __init__(self, *args, **kwargs):
        super(GalleryField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': GalleryChoiceField}
        defaults.update(kwargs)
        return super(GalleryField, self).formfield(**defaults)
