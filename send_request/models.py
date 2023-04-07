from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class SendModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    number_of_form = models.PositiveSmallIntegerField()
    form_name = models.CharField(max_length=50)
    token = models.CharField(max_length=255)
    channel_id = models.CharField(max_length=25)
    urls_pictures = models.TextField(max_length=500)
    text = models.TextField(max_length=5000)

    class Meta:
        verbose_name = _("form to send")
        verbose_name_plural = _("forms to send")

    def __str__(self):
        return f'{self.number_of_form} {self.user}'
