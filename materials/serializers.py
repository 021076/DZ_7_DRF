from rest_framework import serializers
from materials.models import LearningCourse, Lesson


class LearningCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningCourse
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'