from django.db import models

from apps.utils.models import AbstractBaseModel


class PaymentMethod(AbstractBaseModel):
    name = models.CharField(max_length=15, unique=True)


    def __str__(self):
        return self.name