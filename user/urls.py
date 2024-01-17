from django.urls import path
from .views import OwnerSignUpView, UserLoginView, RegisterEmployeeView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register', OwnerSignUpView.as_view(), name='owner_sign_up'),
    path('employee', RegisterEmployeeView.as_view(), name='register_employee'),
    path('login', UserLoginView.as_view(), name='user_login'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
