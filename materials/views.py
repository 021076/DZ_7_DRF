from rest_framework import viewsets, generics
from materials.models import LearningCourse, Lesson
from materials.serializers import LearningCourseSerializer, LessonSerializer


# Реализации CRUD для курса через viewsets
class LearningCourseViewSet(viewsets.ModelViewSet):
    serializer_class = LearningCourseSerializer
    queryset = LearningCourse.objects.all()


# Реализации CRUD для урока через generics
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
