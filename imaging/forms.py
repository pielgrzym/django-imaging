from django import forms
from imaging.models import Image
from imaging.widgets import AjaxImageSelection

class AjaxUploadForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude = ( 'content_type', 'content_object', 'object_id', 'ordering')

class GalleryChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        # we need to pass destination model to the widget
        # so we can construct url to destination model form
        dest_model = kwargs.pop('dest_model') # remove dest_model from kwargs so widget won't complain
        super(GalleryChoiceField, self).__init__(*args, **kwargs) # superclass will init our widget class
        self.widget._dest_model = dest_model # we can add dest model to widget object

    widget = AjaxImageSelection
