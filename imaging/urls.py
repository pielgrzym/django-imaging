from django.conf.urls.defaults import *

urlpatterns = patterns('imaging.views',
    (r'^iframe_form/$', 'iframe_form'),
    (r'^ajax_delete/$', 'ajax_image_removal'),
    )
