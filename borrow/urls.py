from django.urls import path
from .views import (
    BorrowRequestView,
    ApproveBorrow,
    RejectBorrow,
    ReturnBorrow,
)

urlpatterns = [
    path('borrow/', BorrowRequestView.as_view()),

    path('borrow/<int:pk>/approve/', ApproveBorrow.as_view()),
    path('borrow/<int:pk>/reject/', RejectBorrow.as_view()),
    path('borrow/<int:pk>/return/', ReturnBorrow.as_view()),
]