from django.db import models


class Scheme(models.Model):
    CATEGORY_CHOICES = [
        ('Farmers', 'Farmers'),
        ('General', 'General'),
        ('Women', 'Women'),
        ('Students', 'Students'),
        ('BPL', 'BPL'),
    ]

    name = models.CharField(max_length=200)
    ministry = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()   # About this scheme
    benefits = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
