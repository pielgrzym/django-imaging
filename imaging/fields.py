from django.db import models
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
    def formfield(self, **kwargs):
        defaults = {'form_class': GalleryChoiceField,
                'dest_model': self.related.parent_model.__name__.lower()}
        defaults.update(kwargs)
        return super(GalleryField, self).formfield(**defaults)
