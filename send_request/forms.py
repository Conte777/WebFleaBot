from django.forms import ModelForm, URLField
from send_request.models import SendModel, URLarray
from django.utils.translation import gettext_lazy as _


class SendForm(ModelForm):
    class Meta:
        model = SendModel
        fields = ['form_name', 'token', 'channel_id', 'text']


class URLsForm(ModelForm):
    url = URLField(required=False, label=_("URL of picture"))

    class Meta:
        model = URLarray
        fields = ['url']
