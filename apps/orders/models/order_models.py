from django.db import models
from django.conf import settings

from apps.utils.models import AbstarBaseModel


# Create your models here.
class Order(AbstarBaseModel):
    coupon = models.ForeignKey(to='Coupon', on_delete=models.PROTECT)
    payment_method = models.ForeignKey(to='general.PaymentMethod', on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    total_price = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      default=0)
    store_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True,
                                   blank=True)
    delivery_price = models.DecimalField(max_digits=10,
                                         decimal_places=2,
                                         default=0)


    def __str__(self):
        return f"user {self.user.id}"


class OrderProduct(AbstarBaseModel):
    quantity = models.IntegerField()
    order = models.ForeignKey(to='Order', on_delete=models.PROTECT)
    book = models.ForeignKey(to="Book", on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0)

