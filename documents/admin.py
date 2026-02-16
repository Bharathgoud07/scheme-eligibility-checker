from django.contrib import admin
from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name','category')
    search_fields = ('name', 'category')
    list_filter = ('category',)
