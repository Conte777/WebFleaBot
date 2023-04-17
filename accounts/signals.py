from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import UserModel
from send_request.models import SendModel


@receiver(post_save, sender=UserModel)
def create_sendmodels(sender, **kwargs):
    if kwargs['created']:
        for i in range(1, kwargs['instance'].number_sending_models + 1):
            SendModel.objects.create(
                user=kwargs['instance'], form_name=str(i))