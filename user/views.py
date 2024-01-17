from .models import User
from .serializers import OwnerSignUpSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

class OwnerSignUpView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = OwnerSignUpSerializer
