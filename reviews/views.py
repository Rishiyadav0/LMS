from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BookReview
from .serializers import ReviewSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import JSONParser

class ReviewView(APIView):
    
    def get(self, request, book_id):
        reviews = BookReview.objects.filter(book_id=book_id)
        return Response(ReviewSerializer(reviews, many=True).data)

    @swagger_auto_schema(request_body=ReviewSerializer)
    def post(self, request, book_id):
        if not request.user.is_authenticated:
            return Response({"detail": "Login required"}, status=401)

        data = request.data.copy()
        data['book'] = book_id

        serializer = ReviewSerializer(data=data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)