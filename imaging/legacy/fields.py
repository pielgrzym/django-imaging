from django.db import models
from django.db.models.signals import post_save
#from django.forms import widgets
from imaging.models import Image
from django.contrib.contenttypes import generic

from imaging.legacy.forms import CommaSeparatedIntField

def save_relations(sender, **kwargs):
    '''Take care about image order and image connection to a model'''
    value_dict = getattr(kwargs['instance'], kwargs['instance']._imaging_fname).split(",")
    for i, v in enumerate(value_dict):
        try:
            image = Image.objects.get(pk=v)
            image.ordering = i
            image.content_object = kwargs['instance']
            image.save()
        except:
            pass


class ImagingField(models.Field):
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        kwargs['default'] = ''
        super(ImagingField, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name):
        super(ImagingField, self).contribute_to_class(cls, name)
        #content_type = ContentType.objects.get_for_model(cls)
        setattr(cls, self.name+"_set2", generic.GenericRelation(Image))

    def pre_save(self, model_instance, add):
        # set a new attribute which hold the field from which we take id later on
        setattr(model_instance, '_imaging_fname', self.name)
        # connect a new signal
        post_save.connect(save_relations, sender=model_instance.__class__)
        return getattr(model_instance, self.attname)

    def db_type(self, connection=None):
        return 'char(255)'

    def formfield(self, **kwargs):
        defaults = {'form_class': CommaSeparatedIntField}
        defaults.update(kwargs)
        return super(ImagingField, self).formfield(**defaults)
