from django.db import models
from schemes.models import Scheme


class EligibilityRule(models.Model):
    OPERATOR_CHOICES = [
        ('<=', '<='),
        ('>=', '>='),
        ('IN', 'IN'),
    ]

    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE, related_name='rules')
    field_name = models.CharField(
        max_length=50,
        help_text="Profile field name (age, annual_income, category, education_level) or 'document'"
    )
    operator = models.CharField(max_length=5, choices=OPERATOR_CHOICES)
    value = models.JSONField(
        help_text="For document rules use list of document names. For others use value or list."
    )
    message = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.scheme.name} - {self.field_name}"
