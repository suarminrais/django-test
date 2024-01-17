from django.urls import path
from .views import OwnerSignUpView


urlpatterns = [
    path('register/', OwnerSignUpView.as_view(), name='owner_sign_up'),
]
