from django.urls import path
from .views import ReviewView

urlpatterns = [
    path('books/<int:book_id>/reviews/', ReviewView.as_view()),
]