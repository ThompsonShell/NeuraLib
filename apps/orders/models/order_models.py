from django.db import models
from django.conf import settings

from apps.utils.models import AbstarBaseModel
from apps.books.models.book_models import Book

# Create your models here.
class Order(AbstarBaseModel):
    coupon = models.ForeignKey(
        to='orders.Coupon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    payment_method = models.ForeignKey(
        to='general.PaymentMethod',
        on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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


class OrderBook(AbstarBaseModel):
    quantity = models.IntegerField()
    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
        related_name = 'order_books'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0)
