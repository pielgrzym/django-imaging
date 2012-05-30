from django.conf.urls.defaults import *

urlpatterns = patterns('imaging.views',
    url(r'^iframe_form/$', 'iframe_form', name="imaging_iframe_form"),
    url(r'^ajax_delete/$', 'ajax_image_removal', name="imaging_image_removal"),
    )
