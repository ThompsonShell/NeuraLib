from django.contrib import admin
from .models.user_models import CustomUser


class UserManager(admin.ModelAdmin):
    model = CustomUser
    admin.site.register(CustomUser)