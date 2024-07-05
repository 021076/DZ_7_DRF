from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


class LearningCourse(models.Model):
    objects = None
    title = models.CharField(max_length=150, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    imagery = models.ImageField(upload_to='products/', verbose_name='Изображение(превью)', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Учебный курс'
        verbose_name_plural = 'Учебные курсы'


class Lesson(models.Model):
    objects = None
    name = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    course = models.ForeignKey(LearningCourse, on_delete=models.CASCADE, verbose_name='Учебный курс')
    imagery = models.ImageField(upload_to='products/', verbose_name='Изображение(превью)', **NULLABLE)
    video = models.URLField(max_length=150, verbose_name='Ссылка на видео', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
