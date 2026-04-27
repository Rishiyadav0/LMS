from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BorrowRequest


@receiver(post_save, sender=BorrowRequest)
def update_book_copies(sender, instance, **kwargs):
    book = instance.book

    if instance.status == "APPROVED":
        book.available_copies -= 1
        book.save()

    elif instance.status == "RETURNED":
        book.available_copies += 1
        book.save()