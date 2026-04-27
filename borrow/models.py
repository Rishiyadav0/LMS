from django.db import models
from django.conf import settings
from books.models import Book

# Create your models here.

class BorrowRequest(models.Model):

    STATUS_CHOICES = (('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('RETURNED', 'Returned'),)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    requested_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.book})"