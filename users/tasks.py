from datetime import datetime, timedelta
from celery import shared_task
import pytz
from config import settings
from users.models import User


@shared_task
def check_activity_user():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    users = User.objects.all()
    for user in users:
        if current_datetime - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
