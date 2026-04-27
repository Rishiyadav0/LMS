from rest_framework import serializers
from .models import BookReview


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = '__all__'
        read_only_fields = ['user']