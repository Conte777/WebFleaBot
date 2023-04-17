from django.forms import ModelForm
from .models import UserModel
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm


class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = UserModel
        fields = ("username", "email")


class ToggleSendForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['is_send_active']


class UserChangeForm(BaseUserChangeForm):
    class Meta(BaseUserChangeForm.Meta):
        model = UserModel
