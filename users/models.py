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
    date_payment = models.DateField(auto_now=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(LearningCourse, on_delete=models.CASCADE, verbose_name='Курс')
    payment_method = models.CharField(max_length=15, choices=PAYMENT_METHOD, verbose_name='Способ оплаты')
    amount = models.PositiveIntegerField(default=0, verbose_name='Сумма платежа')
    id_session = models.CharField(max_length=255, verbose_name='Id сессии', **NULLABLE)
    link_to_pay = models.URLField(max_length=400, verbose_name='Ссылка на оплату', **NULLABLE)

    def __str__(self):
        return f'{self.user} {self.amount} {self.date_payment} {self.course} {self.payment_method}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
