from datetime import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.utils.models import AbstractBaseModel


class Coupon(AbstractBaseModel):
    title = models.CharField(max_length=70)
    slug = models.SlugField()
    code = models.CharField(max_length=15, unique=True)
    expiration_date = models.DateTimeField()
    
    discount_in_percent = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1),
                    MaxValueValidator(100)
                    ]
        )


    def check_coupon_date(self):
        return self.expiration_date <= timezone.now()
