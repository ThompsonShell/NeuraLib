from django.db import models
from django.db.models import PROTECT
from apps.users.models.user_models import CustomUser


class Article(models.Model):
    author = models.ForeignKey(
        to=CustomUser,
        on_delete=PROTECT,
        related_name='articles',
        limit_choices_to={'role': CustomUser.Role.AUTHOR}
        )
    
    title = models.CharField(max_length=500)
    text = models.TextField(max_length=100_000_000)
    comment = models.CharField(max_length=10000)
    image = models.FileField(upload_to='article/image')
    published_at = models.DateTimeField()





