from django.db import models
from django.core.validators import FileExtensionValidator
from book_category.models import BookCategory


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(
        upload_to="book_images",
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])
        ],  # Valid image formats
    )
    video = models.FileField(
        upload_to="book_videos",
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["mp4", "avi", "mkv"])
        ],  # Valid video formats
    )
    downloadable = models.BooleanField(default=False)
    category = models.ForeignKey(
        BookCategory, on_delete=models.SET_DEFAULT, default=None
    )
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
