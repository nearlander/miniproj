from django.db import models

class UserProfile(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('SAVINGS', 'Savings Account'),
        ('CURRENT', 'Current Account'),
        ('STUDENT', 'Student Account'),
        ('JOINT', 'Joint Account'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()
    account_type = models.CharField(
        max_length=20,
        choices=ACCOUNT_TYPE_CHOICES,
        default='SAVINGS'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
