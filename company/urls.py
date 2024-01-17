from django.urls import path
from .views import CompanyCreationView

urlpatterns = [
    path('', CompanyCreationView.as_view(), name='company_creation'),
]
