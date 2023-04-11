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

    urls = send.urlarray_set.all()
    if not urls:
        urls = [None] * SendModel.MAX_URLS

    urslforms = []
    if request.method == 'POST':
        for url in urls:
            urslforms.append(URLsForm(request.POST, instance=url))
        formsend = SendForm(request.POST, instance=send)
        if formsend.is_valid() and all(urlform.is_valid() for urlform in urslforms):
            sendmodel = formsend.save()
            for urlform in urslforms:
                urlmodel = urlform.save(commit=False)
                if urlmodel.url != '':
                    urlmodel.sendmodel = sendmodel
                    urlmodel.save()
            return HttpResponseRedirect(reverse_lazy('home'))

    elif request.method == 'GET':
        for url in urls:
            urslforms.append(URLsForm(instance=url))
        formsend = SendForm(instance=send)

    return render(request, 'send_request/create_edit_sendmodel.html',
                  {'form_send': formsend,
                   'forms_urls': urslforms})
