from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'industry']
    
    def create(self, validated_data):
        company = Company.objects.create(
            name=validated_data['name'], 
            industry=validated_data['industry'], 
            created_by_id=validated_data['owner'].id,
        )
        company.save()

        return company
