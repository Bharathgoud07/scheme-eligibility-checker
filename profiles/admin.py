from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'category', 'annual_income', 'state')
    list_filter = ('category', 'state')
    search_fields = ('name',)
