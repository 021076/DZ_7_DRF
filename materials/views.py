from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from materials.paginators import AppPagination
from materials.models import LearningCourse, Lesson, Subscription
from materials.serializers import LearningCourseSerializer, LessonSerializer, SubscriptionSerializer
from users.permissions import IsModerator, IsOwner


# Реализации CRUD для курса через viewsets
class LearningCourseViewSet(viewsets.ModelViewSet):
    serializer_class = LearningCourseSerializer
    queryset = LearningCourse.objects.all()
    pagination_class = AppPagination

    def perform_create(self, serializer):
        new_learningcourse = serializer.save()
        new_learningcourse.owner = self.request.user
        new_learningcourse.save()

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = [IsModerator | IsOwner, ]
        elif self.action == 'list':
            self.permission_classes = [IsModerator | IsOwner, ]
        elif self.action == 'update':
            self.permission_classes = [IsModerator | IsOwner, ]
        elif self.action == 'partial_update':
            self.permission_classes = [IsModerator | IsOwner, ]
        elif self.action == 'create':
            self.permission_classes = [~IsModerator, ]
        elif self.action == 'destroy':
            self.permission_classes = [~IsModerator | IsOwner, ]
        return super().get_permissions()


# Реализации CRUD для урока через generics
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator, ]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner, ]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerator | IsOwner, ]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ]
    pagination_class = AppPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_obj = get_object_or_404(LearningCourse, pk=course_id)
        subscription_obj = Subscription.objects.filter(user=user, course=course_obj)
        if subscription_obj.exists():
            subscription_obj.delete()
            message = 'Подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course_obj)
            message = 'Подписка добавлена'
        return Response({"message": message})


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]
