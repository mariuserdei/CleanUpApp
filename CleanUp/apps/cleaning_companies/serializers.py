from django.db.models import fields
from rest_framework import serializers
from .models import CleaningCompany

class CleaningCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CleaningCompany
        # fields = ['name', 'email', 'phone_number']
        fields = '__all__'