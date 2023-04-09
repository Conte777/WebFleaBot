from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from send_request.models import SendModel
from .forms import SendForm


@login_required
def create_edit_sendmodel(request: HttpRequest, model_id):
    try:
        send = request.user.sendmodel_set.get(id=model_id)
    except SendModel.DoesNotExist:
        return HttpResponse('Нет такого объекта у этого пользователя')

    if request.method == 'POST':
        form = SendForm(request.POST, instance=send)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('home'))
    elif request.method == 'GET':
        form = SendForm(instance=send)

    return render(request, 'send_request/create_edit_sendmodel.html', {'form': form})
