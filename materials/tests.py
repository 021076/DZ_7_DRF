from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from materials.models import LearningCourse, Lesson
from users.models import User


class LessonsAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@user.com', password='123456')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.course = LearningCourse.objects.create(
            title="Тестовый курс", description="Тестовый курс для тестирования")
        self.lesson = Lesson.objects.create(
            name="Урок", description="Описание урока", course=self.course)

    def test_lesson_create(self):
        """Юниттест создания урока"""
        db_create = {
            "name": "Тестовый урок",
            "description": "Тестовый урок для тестирования",
            "course": self.course.pk
        }
        create_response = self.client.post("/materials/lesson/create/", db_create)
        # print(f'лог: {create_response.json()}')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Lesson.objects.filter(name="Тестовый урок").count(), 1
        )

    def test_lessons_list_get(self):
        """Юниттест вывода списка уроков"""
        get_response = self.client.get("/materials/lessons_list/")
        # print(f'лог: {get_response.json()}')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            get_response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': self.lesson.pk, 'name': 'Урок', 'description': 'Описание урока', 'imagery': None, 'video': None,
                 'course': self.course.pk,
                 'owner': None}]}
        )

    def test_lesson_retrieve(self):
        """Юниттест вывода детализации урока"""
        url = reverse("materials:lesson", kwargs={'pk': self.lesson.pk})
        detail_response = self.client.get(url)
        # print(f'лог: {detail_response.json()}')
        self.assertEqual(detail_response.status_code, status.HTTP_200_OK)
        self.assertEqual(detail_response.data['name'], 'Урок')

    def test_lesson_delete(self):
        """Юниттест уаделния урока"""
        url = reverse("materials:lesson_destroy", kwargs={'pk': self.lesson.pk})
        del_response = self.client.delete(url)
        # print(f'лог: {del_response}')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)

    def test_lesson_put(self):
        """Юниттест обновления урока через put"""
        db_put = {
            "name": "Измененный урок",
            "description": "Описание измененного урока",
            "course": self.course.pk
        }
        url = reverse("materials:lesson_update", kwargs={'pk': self.lesson.pk})
        put_response = self.client.put(url, db_put)
        # print(f'лог: {put_response}')
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(put_response.data['name'], "Измененный урок")

    def test_lesson_patch(self):
        """Юниттест обновления урока через patch"""
        db_patch = {
            "name": "Урок с видео",
            "video": "https://www.youtube.com/video/Fdf454sd"
        }
        url = reverse("materials:lesson_update", kwargs={'pk': self.lesson.pk})
        patch_response = self.client.patch(url, db_patch)
        # print(f'лог: {put_response}')
        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_response.data['name'], "Урок с видео")
        self.assertEqual(patch_response.data['video'], "https://www.youtube.com/video/Fdf454sd")


class SubscriptionAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@user.com', password='123456')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.course = LearningCourse.objects.create(
            title="Тестовый курс", description="Тестовый курс для тестирования")

    def test_subscription_create(self):
        """Юниттест создания подписки"""
        url = reverse("materials:subscription_create")
        db_create = {"user": self.user.id, "course": self.course.id}
        # create_response = self.client.post("materials/subscription/create/", db_create)
        create_response = self.client.post(url, db_create)
        # print(f'лог: {create_response.json()}')
        self.assertEqual(create_response.status_code, status.HTTP_200_OK)
        self.assertEqual(create_response.json(), {'message': 'Подписка добавлена'})

    def test_subscription_delete(self):
        """Юниттест создания подписки"""
        url = reverse("materials:subscription_create")
        db_create = {"user": self.user.id, "course": self.course.id}
        # сначала создали подписку
        self.client.post(url, db_create)
        # потом удалили подписку
        del_response = self.client.post(url, db_create)
        # print(f'лог: {del_response.json()}')
        self.assertEqual(del_response.status_code, status.HTTP_200_OK)
        self.assertEqual(del_response.json(), {'message': 'Подписка удалена'})
