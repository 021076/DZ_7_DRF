from django.urls import path
from rest_framework.routers import DefaultRouter
from materials.apps import MaterialsConfig
from materials.views import LearningCourseViewSet, LessonCreateAPIView, LessonUpdateAPIView, LessonDestroyAPIView, \
    LessonListAPIView, LessonRetrieveAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'learningcourse', LearningCourseViewSet, 'learningcourse')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name="lesson_create"),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name="lesson_update"),
                  path('lesson/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name="lesson_destroy"),
                  path('lessons_list/', LessonListAPIView.as_view(), name="lessons_list"),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name="lesson"),
                  path('subscription/create/', SubscriptionCreateAPIView.as_view(), name="subscription_create"),
                  path('subscription/destroy/<int:pk>/', SubscriptionDestroyAPIView.as_view(),
                       name="subscription_destroy"),
              ] + router.urls
