import re

from rest_framework.serializers import ValidationError


class VideoValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        check_field = dict(value).get(self.field)
        if "www.youtube.com" not in check_field:
            raise ValidationError('Недопустимая ссылка')
