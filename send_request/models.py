from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class SendModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    form_name = models.CharField(_("form name"), max_length=50)
    token = models.CharField(_("token of discord account"), max_length=255)
    channel_id = models.CharField(_("ID of discord channel"), max_length=25)
    text = models.TextField(_("text for messege"), max_length=5000)

    MAX_URLS = 3

    class Meta:
        verbose_name = _("form to send")
        verbose_name_plural = _("forms to send")

    def __str__(self):
        return f'{self.id} {self.user}'


class URLarray(models.Model):
    url = models.URLField(_("URL of picture"))
    sendmodel = models.ForeignKey(SendModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.url

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.url != '':
            return super().save(force_insert, force_update, using, update_fields)
        else:
            self.delete()

    class Meta:
        verbose_name = _("URL for send model")
        verbose_name_plural = _("URLs for send model")
