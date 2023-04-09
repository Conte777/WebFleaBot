from django.forms import ModelForm
from . import models


class SendForm(ModelForm):
    class Meta:
        model = models.SendModel
        fields = ['form_name', 'token', 'channel_id', 'text']
