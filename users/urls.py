from django.urls import path
from users.apps import UsersConfig
from users.views import PaymentsListAPIView, UserCreateAPIView, UserUpdateAPIView, \
    UserDestroyAPIView, UserListAPIView, UserRetrieveAPIView, PaymentsCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

urlpatterns = ([
    path('payments_list/', PaymentsListAPIView.as_view(), name="payments_list"),
    path('payment/create/', PaymentsCreateAPIView.as_view(), name="payment_create"),
    path('user/create/', UserCreateAPIView.as_view(), name="user_create"),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name="user_update"),
    path('user/destroy/<int:pk>/', UserDestroyAPIView.as_view(), name="user_destroy"),
    path('users_list/', UserListAPIView.as_view(), name="users_list"),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name="user"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
)
