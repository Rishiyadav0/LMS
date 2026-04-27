from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404

from .models import BorrowRequest
from .serializers import BorrowSerializer
from books.models import Book
from books.permissions import IsLibrarian


class BorrowRequestView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request):
        qs = BorrowRequest.objects.filter(user=request.user)
        return Response(BorrowSerializer(qs, many=True).data)

    @swagger_auto_schema(request_body=BorrowSerializer)
    def post(self, request):
        serializer = BorrowSerializer(data=request.data)

        if serializer.is_valid():
            book = serializer.validated_data['book']

            if book.available_copies <= 0:
                return Response({"detail": "No copies available"}, status=400)

            serializer.save(user=request.user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
    
class ApproveBorrow(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties={}))
    def patch(self, request, pk):
        if request.user.role != "LIBRARIAN":
            return Response({"detail": "Not allowed"}, status=403)

        obj = get_object_or_404(BorrowRequest, pk=pk)

        if obj.status != "PENDING":
            return Response({"detail": "Already processed"}, status=400)

        obj.status = "APPROVED"
        obj.save()

        return Response({"message": "Approved"})
    
class RejectBorrow(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties={}))
    def patch(self, request, pk):
        if request.user.role != "LIBRARIAN":
            return Response({"detail": "Not allowed"}, status=403)

        obj = get_object_or_404(BorrowRequest, pk=pk)

        obj.status = "REJECTED"
        obj.save()

        return Response({"message": "Rejected"})
    
class ReturnBorrow(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties={}))
    def patch(self, request, pk):
        obj = get_object_or_404(BorrowRequest, pk=pk)

        if obj.user != request.user:
            return Response({"detail": "Not your request"}, status=403)

        obj.status = "RETURNED"
        obj.save()

        return Response({"message": "Returned"})