from django.forms import inlineformset_factory
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import SendModel, URLarray
from .forms import SendForm, URLsForm


@login_required
def create_edit_sendmodel(request: HttpRequest, model_id):
    try:
        send = request.user.sendmodel_set.get(id=model_id)
    except SendModel.DoesNotExist:
        return HttpResponse('Нет такого объекта у этого пользователя')

    URLFormSet = inlineformset_factory(
        SendModel, URLarray, form=URLsForm, extra=SendModel.MAX_URLS, max_num=SendModel.MAX_URLS, can_delete=False)

    if request.method == 'POST':
        FormSet = URLFormSet(request.POST, instance=send,
                             queryset=send.urlarray_set.all())
        formsend = SendForm(request.POST, instance=send)
        if formsend.is_valid() and FormSet.is_valid():
            FormSet.save()
            formsend.save()
            return HttpResponseRedirect(reverse_lazy('home'))

    elif request.method == 'GET':
        FormSet = URLFormSet(instance=send,
                             queryset=send.urlarray_set.all())
        formsend = SendForm(instance=send)

    return render(request, 'send_request/create_edit_sendmodel.html',
                  {'form_send': formsend,
                   'forms_urls': FormSet})
