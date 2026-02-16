from django.db import models
from profiles.models import UserProfile


class Document(models.Model):

    CATEGORY_CHOICES = [
        ("identity", "Identity Documents"),
        ("income", "Income Proof"),
        ("other", "Other Documents"),
        ("residence", "Residence Proof"),
        ("education", "Education Documents"),
    ]

    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class UserDocument(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('profile', 'document')
