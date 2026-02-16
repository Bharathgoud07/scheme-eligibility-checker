from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    CASTE_CHOICES = [
        ('GENERAL', 'General'),
        ('OBC', 'OBC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=100)

    caste_status = models.CharField(
        max_length=10,
        choices=CASTE_CHOICES,
        default='GENERAL'
    )

    is_bpl = models.BooleanField(default=False)
    is_farmer = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_woman = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Profile"


class Scheme(models.Model):

    CATEGORY_CHOICES = [
        ('General', 'General'),
        ('BPL', 'BPL'),
        ('Women', 'Women'),
        ('Students', 'Students'),
        ('Farmers', 'Farmers'),
        ('Youth', 'Youth'),
    ]

    SCHEME_CATEGORY_CHOICES = [
        ('Education', 'Education'),
        ('Health', 'Health'),
        ('Employment', 'Employment'),
        ('Housing', 'Housing'),
        ('Finance', 'Finance'),
        ('Women & Child', 'Women & Child'),
        ('Agriculture', 'Agriculture'),
        ('Social Welfare', 'Social Welfare'),
    ]

    name = models.CharField(max_length=255)
    ministry = models.CharField(max_length=255)

    description = models.TextField()
    benefits = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='General'
    )

    scheme_category = models.CharField(
        max_length=50,
        choices=SCHEME_CATEGORY_CHOICES,
        default='General'
    )

    target_group = models.CharField(max_length=100, blank=True)

    # JSON criteria like:
    # {"min_age":18, "max_income":200000, "requires_bpl":true}
    eligibility_criteria = models.JSONField(default=dict, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SchemeDocument(models.Model):

    scheme = models.ForeignKey(
        Scheme,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_required = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.scheme.name} - {self.name}"
