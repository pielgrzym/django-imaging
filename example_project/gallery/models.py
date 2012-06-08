from django.db import models

from django.contrib.contenttypes import generic
from imaging.fields import ImagingField, GalleryField
from imaging.models import Image, ImageAbstract, GalleryAbstract

class Gallery(models.Model):
    name = models.CharField(max_length=255)
    photos = ImagingField()
    photos_set = generic.GenericRelation(Image)

class Student(ImageAbstract):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

class SchoolStudent(GalleryAbstract):
    GR = ['student', 'schoolclass']
    student = models.ForeignKey(Student)
    schoolclass = models.ForeignKey('SchoolClass')

class SchoolClass(models.Model):
    name = models.CharField(max_length=255)
    students = GalleryField(Student, through=SchoolStudent)
