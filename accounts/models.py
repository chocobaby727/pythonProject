from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'

    email = models.EmailField('メールアドレス', unique=True, error_messages={'unique': 'このメールアドレスを持ったユーザーが既に存在します。'})
