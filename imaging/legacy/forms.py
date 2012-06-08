from django import forms
from imaging.legacy.widgets import ImageSelection
from django.utils.translation import ugettext as _

class CommaSeparatedIntField(forms.CharField):
    widget = ImageSelection
    def clean(self, value):
        value = super(CommaSeparatedIntField, self).clean(value)
        if value == u'':
            return value
        valuelist = ['0','1','2','3','4','5','6','7','8','9', ',']
        for char in value:
            if char not in valuelist:
                raise forms.ValidationError(_("Image field error, please contact administrator"))
        return value

