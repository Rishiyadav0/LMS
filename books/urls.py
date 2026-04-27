from django.urls import path
from .views import BookListCreate, BookDetail, AuthorListCreate, GenreListCreate

urlpatterns = [
    # authors
    path('authors/', AuthorListCreate.as_view()),

    # genres
    path('genres/', GenreListCreate.as_view()),
    # books
    path('books/', BookListCreate.as_view()),
    path('books/<int:pk>/', BookDetail.as_view()),

]