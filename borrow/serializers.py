from rest_framework import serializers
from .models import BorrowRequest


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRequest
        fields = '__all__'
        read_only_fields = ['user', 'status']