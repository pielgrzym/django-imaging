from imaging.legacy.views import iframe_form, ajax_image_removal
from django.forms.models import modelform_factory, ModelForm
from django.http import Http404
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def gallery_iframe_form(request, modelname):
    from imaging import galleries
    if galleries.has_model(modelname):
        model = galleries.registry[modelname]
        form = modelform_factory(model, model.get_form() or ModelForm)
    else:
        raise Http404()
    return render_to_response('imaging/iframe_form.html',
            { 'form' : form },
            context_instance=RequestContext(request))
