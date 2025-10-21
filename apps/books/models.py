from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.db import models, transaction
from django.utils.text import slugify
from rest_framework.exceptions import ValidationError

from apps.utils.models import AbstarBaseModel


class BookGenre(models.TextChoices):
    FICTION = "fiction", "Fiction"
    SCIENCE = "science", "Science"
    FANTASY = "fantasy", "Fantasy"
    MYSTERY = "mystery", "Mystery"
    ROMANCE = "romance", "Romance"
    BIOGRAPHY = "biography", "Biography"
    SELF = "self", "Self"
    HISTORY = "history", "History"


class Book(AbstarBaseModel):
    title = models.CharField(min_length=3, max_length=250)
    slug = models.SlugField(
        max_length=250,
        editable=False
    )
    # author = models.ForeignKey()
    pages = models.PositiveIntegerField(null=True, blank=True)
    pdf = models.FileField(upload_to='/books/pdf', validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True, blank=True)
    audio = models.FileField(upload_to='/books/audio', validators=[FileExtensionValidator(allowed_extensions=['mp3'])], null=True, blank=True)
    published_at = models.DateField(help_text="Original publication date of the book")
    description = models.TextField(max_length=10_000, blank=True, help_text="Book summary or description")
    rating = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    genre = models.CharField(choices=BookGenre.choices, default="Fiction", max_length=30)
    is_available = models.BooleanField(default=True, help_text="Is the book available for reading")


    def clean(self):
        if not self.slug:
            self.slug = slugify(self.title)

        if Book.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            raise ValidationError("A book with this name already exists !")

    def __str__(self):
        return f"name {self.title} author {self.author} published time{self.published_at}"

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

        @transaction.on_commit
        def remove_pdf():
            self.pdf.delete(save=False)


    def check_published_book(self):
        if self.published_at >= datetime.now():
            raise ValueError("The published time of book did not high from at the time")