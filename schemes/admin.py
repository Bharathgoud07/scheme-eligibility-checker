from django.contrib import admin
from .models import Scheme
from rules.models import EligibilityRule


class EligibilityRuleInline(admin.TabularInline):
    model = EligibilityRule
    extra = 1
    fields = ('field_name', 'operator', 'value', 'message')


@admin.register(Scheme)
class SchemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'ministry', 'category', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'ministry')
    inlines = [EligibilityRuleInline]
