from .models import UserModel
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
# from send_request.models import SendModel


class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = UserModel
        fields = ("username", "email")

    # def save(self, commit=True):
    #     user = super().save()
    #     user.create_sendmodels()
    #     return user


class UserChangeForm(BaseUserChangeForm):
    class Meta(BaseUserChangeForm.Meta):
        model = UserModel
