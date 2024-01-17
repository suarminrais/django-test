from .models import User
from .serializers import OwnerSignUpSerializer, UserLoginSerializer, RegisterEmployee
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class OwnerSignUpView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = OwnerSignUpSerializer

class UserLoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

class RegisterEmployeeView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RegisterEmployee

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
