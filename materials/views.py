from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.models import LearningCourse, Lesson
from materials.serializers import LearningCourseSerializer, LessonSerializer


# Реализации CRUD для курса через viewsets
class LearningCourseViewSet(viewsets.ModelViewSet):
    serializer_class = LearningCourseSerializer
    queryset = LearningCourse.objects.all()

    def perform_create(self, serializer):
        new_learningcourse = serializer.sev
        new_learningcourse.owner = self.request.user.is_staff
        new_learningcourse.save()


# Реализации CRUD для урока через generics
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.sev
        new_lesson.owner = self.request.user.is_staff
        new_lesson.save()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
