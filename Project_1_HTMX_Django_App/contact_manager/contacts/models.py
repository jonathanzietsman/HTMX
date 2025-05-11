from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

# Create your models here.

class Contact(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2, message="Name must be at least 2 characters long."),
            MaxLengthValidator(100, message="Name cannot exceed 100 characters."),
        ],
        help_text="Enter the contact's full name (2-100 characters)"
    )
    email = models.EmailField(
        max_length=254,
        help_text="Enter a valid email address"
    )
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
        help_text="Enter a valid phone number (9-15 digits, optionally starting with +)"
    )
    address = models.TextField(
        blank=True,
        max_length=500,
        validators=[
            MaxLengthValidator(500, message="Address cannot exceed 500 characters.")
        ],
        help_text="Enter the contact's address (optional, max 500 characters)"
    )
    notes = models.TextField(
        blank=True,
        max_length=1000,
        validators=[
            MaxLengthValidator(1000, message="Notes cannot exceed 1000 characters.")
        ],
        help_text="Enter any additional notes (optional, max 1000 characters)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
