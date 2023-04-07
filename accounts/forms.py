from .models import UserModel
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from send_request.models import SendModel


class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = UserModel
        fields = ("username", "email")

    def save(self, commit=True):
        user = super().save()
        for i in range(1, user.number_sending_models + 1):
            SendModel.objects.create(
                user=user, number_of_form=i, form_name=str(i))
        return user


class UserChangeForm(BaseUserChangeForm):
    class Meta(BaseUserChangeForm.Meta):
        model = UserModel
