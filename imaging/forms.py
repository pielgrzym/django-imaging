from django import forms
from imaging.models import Image
from imaging.widgets import AjaxImageSelection

class AjaxUploadForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude = ( 'content_type', 'content_object', 'object_id', 'ordering')

class GalleryChoiceField(forms.ModelMultipleChoiceField):
    widget = AjaxImageSelection
