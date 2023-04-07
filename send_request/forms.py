from django.forms import ModelForm
from .models import SendModel


class SendForm(ModelForm):
    class Meta:
        model = SendModel
        fields = ['form_name', 'token', 'channel_id', 'urls_pictures', 'text']
