from django.db.models import fields
from rest_framework import serializers
from .models import Cities

class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['name', 'zip_code']