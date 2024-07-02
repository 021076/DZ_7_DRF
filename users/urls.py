from django.urls import path
from users.apps import UsersConfig
from users.views import PaymentsListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('payments_list/', PaymentsListAPIView.as_view(), name="payments_list"),
]