from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from materials.models import Subscription, LearningCourse
from users.models import User


@shared_task
def send_mail_update_course(course_id):
    subscriptions = Subscription.objects.filter(course_id=course_id)
    if subscriptions:
        list_email = []
        course_title = LearningCourse.objects.get(pk=course_id).title
        for obj in subscriptions:
            email = User.objects.get(pk=obj.user_id).email
            list_email.append(email)
        send_mail(f'Обновление курса "{course_title}"',
                  f'Вы подписаны на обновление курсов.\nУведомляем об обновлении курса "{course_title}"',
                  EMAIL_HOST_USER,
                  list_email,
                  )
