from django.db import models
from datetime import date

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100, blank=True, null=True)
    publication_year = models.PositiveIntegerField()
    is_borrowed = models.BooleanField(default=False)
    borrower_name = models.CharField(max_length=255, blank=True, null=True)
    borrow_date = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Validate publication year
        if self.publication_year > date.today().year:
            raise ValueError("Publication year cannot be in the future.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

