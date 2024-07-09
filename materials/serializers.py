from rest_framework import serializers
from materials.models import LearningCourse, Lesson, Subscription
from materials.validators import VideoValidator


class LearningCourseSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    subscriptions = serializers.SerializerMethodField()

    def get_lessons(self, course):
        lessons_count = Lesson.objects.filter(course=course).count()
        lessons_list = [lesson.name for lesson in Lesson.objects.filter(course=course)]
        return {"lessons_count": lessons_count, "lessons_list": lessons_list}

    def get_subscriptions(self, course):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Subscription.objects.filter(user=request.user, course=course).exists()
        return False

    class Meta:
        model = LearningCourse
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoValidator(field='video')]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
