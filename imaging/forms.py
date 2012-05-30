from django import forms
from imaging.models import Image

class AjaxUploadForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude = ( 'content_type', 'content_object', 'object_id', 'ordering')
