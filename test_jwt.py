import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LMS.settings')
import django
django.setup()
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.test import RequestFactory
import json

factory = RequestFactory()

# Test 1: Just token
request = factory.get('/api/', HTTP_AUTHORIZATION='eyJhbGci...')
auth = JWTAuthentication()
try:
    header = auth.get_header(request)
    print("Header:", header)
    token = auth.get_raw_token(header)
    print("Raw token:", token)
except Exception as e:
    print("Error:", e)

