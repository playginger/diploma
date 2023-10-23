from django.db import models
from django.contrib.auth.models import AbstractUser



# Модель пользователя
class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)


# Модель записи
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# Модель подписки
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    # Дополнительные поля Stripe для хранения данных платежей
    stripe_customer_id = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)
