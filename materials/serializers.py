from rest_framework import serializers
from materials.models import LearningCourse, Lesson
from materials.validators import VideoValidator


class LearningCourseSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()

    def get_lessons(self, course):
        lessons_count = Lesson.objects.filter(course=course).count()
        lessons_list = [lesson.name for lesson in Lesson.objects.filter(course=course)]
        return {"lessons_count": lessons_count, "lessons_list": lessons_list}

    class Meta:
        model = LearningCourse
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoValidator(field='video')]
