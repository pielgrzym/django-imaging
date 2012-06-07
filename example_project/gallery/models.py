from django.db import models

from django.contrib.contenttypes import generic
from imaging.fields import ImagingField
from imaging.models import Image

class Gallery(models.Model):
    name = models.CharField(max_length=255)
    photos = ImagingField()
    photos_set = generic.GenericRelation(Image)
