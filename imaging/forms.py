from django import forms
from imaging.models import Image
from imaging.widgets import AjaxImageSelection

class AjaxUploadForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude = ( 'content_type', 'content_object', 'object_id', 'ordering')

class GalleryChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        # we need to pass destinatio model to the widget
        # so we can construct url to destination model form
        dest_model = kwargs.pop('dest_model')
        super(GalleryChoiceField, self).__init__(*args, **kwargs)
        self.widget._dest_model = dest_model

    widget = AjaxImageSelection
