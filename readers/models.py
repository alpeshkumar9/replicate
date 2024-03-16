import random
import string
from django.contrib.auth.models import User
from django.db import models


class Readers(models.Model):
    """
    Custom User model for readers registered in the library.
    Extends AbstractUser to utilize Django's built-in authentication system.
    Includes additional fields specific to readers.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    library_card_number = models.CharField(
        max_length=10, unique=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    membership_start_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

    def save(self, *args, **kwargs):
        """
        Override the save method to automatically generate a unique library card number
        for new readers if one hasn't been assigned already.
        """
        if not self.library_card_number:
            while True:
                new_card_number = ''.join(random.choices(
                    string.ascii_uppercase + string.digits, k=10))
                if not Readers.objects.filter(library_card_number=new_card_number).exists():
                    self.library_card_number = new_card_number
                    break
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Reader"
        verbose_name_plural = "Readers"
