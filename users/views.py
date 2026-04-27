from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


# Custom Token View
class CustomTokenView(TokenObtainPairView):

    @swagger_auto_schema(request_body=TokenSerializer)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)