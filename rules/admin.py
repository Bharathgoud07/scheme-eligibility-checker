from django.contrib import admin
from .models import EligibilityRule


@admin.register(EligibilityRule)
class EligibilityRuleAdmin(admin.ModelAdmin):
    list_display = ('scheme', 'field_name', 'operator')
    list_filter = ('operator', 'field_name')
    search_fields = ('scheme__name',)
