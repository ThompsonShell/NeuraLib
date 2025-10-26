from django.conf import settings
from django.db import models
from django.db.models import PROTECT


author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
title = models.CharField(max_length=500)
text = models.TextField(max_length=100_000_000)
comment = models.CharField(max_length=10000)
image = models.FileField(upload_to='article/image')
published_at = models.DateTimeField()





