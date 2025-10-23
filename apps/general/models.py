from django.db import models

from apps.utils.models import AbstarBaseModel


class PaymentMethod(AbstarBaseModel):
    name = models.CharField(max_length=15, unique=True)


    def __str__(self):
        return self.name