from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import JSONParser

from .models import Book, Author, Genre
from .serializers import AuthorSerializer, GenreSerializer, BookSerializer, BookCreateSerializer
from .permissions import IsLibrarian


class AuthorListCreate(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        authors = Author.objects.all()
        return Response(AuthorSerializer(authors, many=True).data)

    @swagger_auto_schema(request_body=AuthorSerializer)
    def post(self, request):
        print(request.headers,'------------------')
        if request.user.role != "LIBRARIAN":
            return Response({"detail": "Only librarians"}, status=403)

        serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

class GenreListCreate(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        Genres = Genre.objects.all()
        return Response(GenreSerializer(Genres, many=True).data)

    @swagger_auto_schema(request_body=GenreSerializer)
    def post(self, request):
        if request.user.role != "LIBRARIAN":
            return Response({"detail": "Only librarians"}, status=403)

        serializer = GenreSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
    
class BookListCreate(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        books = Book.objects.all()

        # simple filtering (human style, not overdone)
        author = request.GET.get('author')
        genre = request.GET.get('genre')

        if author:
            books = books.filter(author__name__icontains=author)

        if genre:
            books = books.filter(genres__name__icontains=genre)

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=BookCreateSerializer)
    def post(self, request):
        if request.user.role != "LIBRARIAN":
            return Response({"detail": "Only librarians can add books"}, status=403)

        serializer = BookCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
    
class BookDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return Response(BookSerializer(book).data)

    @swagger_auto_schema(request_body=BookCreateSerializer)
    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)

        if request.user.role != "LIBRARIAN":
            return Response({"detail": "Not allowed"}, status=403)

        serializer = BookCreateSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    @swagger_auto_schema(request_body=BookCreateSerializer)
    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)

        if request.user.role != "LIBRARIAN":
            return Response({"detail": "Not allowed"}, status=403)

        book.delete()
        return Response({"message": "Deleted"}, status=204)