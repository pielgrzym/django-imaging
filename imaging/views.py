from imaging.legacy.views import iframe_form, ajax_image_removal
from django.forms.models import modelform_factory, ModelForm
from django.http import Http404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import simplejson

def gallery_iframe_form(request, modelname):
    from imaging import galleries
    if galleries.has_model(modelname):
        model = galleries.registry[modelname]
        form = modelform_factory(model, model.get_form() or ModelForm)
    else:
        raise Http404()
    callback = None
    if request.method == 'POST':
        form = form(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save()
            response_dict = {
                    'title':"Image",
                    'id'     :new_item.pk,
                    'image':new_item.imaging_thumbnail.url,
                    }
            callback = simplejson.dumps(response_dict)
            form = form()
    else:
        form = form()
    return render_to_response('imaging/iframe_form.html', {
        'form' : form ,
        'callback': callback
        },
        context_instance=RequestContext(request))
