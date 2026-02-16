from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    CATEGORY_CHOICES = [
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OBC', 'OBC'),
        ('GEN', 'General'),
    ]

    EDUCATION_CHOICES = [
        ('10th', '10th'),
        ('12th', '12th'),
        ('UG', 'UG'),
        ('PG', 'PG'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    annual_income = models.PositiveIntegerField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    education_level = models.CharField(max_length=10, choices=EDUCATION_CHOICES)
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    rural = models.BooleanField(default=False)
    bpl = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
