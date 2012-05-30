from django.utils.html import escape, conditional_escape
from django.utils.translation import ugettext
from django.utils.encoding import StrAndUnicode, force_unicode
from django.utils.safestring import mark_safe
from django.forms.util import flatatt
from django.forms.widgets import Widget

from imaging.models import Image

class ImageSelection(Widget):
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
    images_html = ''
    if len(initial_values) > 0:
      for image in initial_values:
        images_html += '<div class="image_block"><span class="image_id">'+str(image.pk)+'</span><a href="/admin/imaging/image/'+str(image.pk)+'/" target="_blank" class="edit_image">Edit</a><a href="#" class="delete_image">Delete</a><img src="'+image.imaging_thumbnail.url+'" alt="'+image.alt+'" /><br /><span class="image_name">'+image.name[:25]+'</span></div>'

    html = '''
    <div class="image_container"> %s </div>

    <div class="iframe_container">
      <iframe src="/imaging/iframe_form/" class="image_upload_form" width="100%%" height="205" frameborder="0"></iframe>
    </div>
    ''' % images_html

    return mark_safe(u'<input type="hidden" class="imaging_data" %s value="%s" /> %s' % (flatatt(final_attrs),
                conditional_escape(force_unicode(value)), html))
