from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import LearningCourse

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payments(models.Model):
    PAYMENT_METHOD = (('Cash', 'Наличные'), ('Transfer', 'Перевод на счет'))
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_payment = models.DateTimeField(auto_now=True, verbose_name='Дата оплаты')
    course_paid = models.ForeignKey(LearningCourse, on_delete=models.CASCADE, verbose_name='Оплаченный курс')
    payment_method = models.CharField(max_length=15, choices=PAYMENT_METHOD, verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.user} {self.date_payment} {self.course_paid} {self.payment_method}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
