from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CompanySerializer

class CompanyCreationView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
