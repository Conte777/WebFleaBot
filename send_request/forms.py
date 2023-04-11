from django.forms import ModelForm
from send_request.models import SendModel, URLarray


class SendForm(ModelForm):
    class Meta:
        model = SendModel
        fields = ['form_name', 'token', 'channel_id', 'text']


class URLsForm(ModelForm):
    class Meta:
        model = URLarray
        fields = ['url']
