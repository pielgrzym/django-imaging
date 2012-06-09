from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.forms.util import flatatt
from django.forms.widgets import Widget
from django.template.loader import render_to_string

from imaging.models import Image
from imaging.legacy.widgets import ImageSelection

class AjaxImageSelection(Widget):
    class Media:
        css = { 'all' : ('imaging/imageselection.css',), }
        js = ('imaging/jquery-1.3.2.min.js',
                'imaging/jquery-ui-1.7.1.custom.min.js',
                'imaging/jquery.json-1.3.min.js',
                'imaging/imageselection.js')

    def render(self, name, value, attrs=None):
        if not value == None:
            value = value.replace(' ', '')
        if value == None or value == '':
            initial_values = []
        else:
            ids = value.split(",")
            initial_values = Image.objects.filter(pk__in=ids)
        value = force_unicode(value)
        final_attrs = self.build_attrs(attrs, name=name)
        template = render_to_string("imaging/admin_widget.html", {
                'existing_images': initial_values, # ask Cpt. Obvious
                'attrs': flatatt(final_attrs), # just for sake of completeness
                'value': conditional_escape(value),
                'dest_model': self._dest_model, # to cunstruct url
                })
        return mark_safe(template)
