from django.contrib import admin
from .models import UserProfile, Scheme, SchemeDocument


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "age",
        "gender",
        "income",
        "is_bpl",
        "is_farmer",
        "is_student"
    )
    list_filter = ("gender", "is_bpl", "is_farmer", "is_student")
    search_fields = ("user__username",)


class SchemeDocumentInline(admin.TabularInline):
    model = SchemeDocument
    extra = 1


@admin.register(Scheme)
class SchemeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "ministry",
        "category",
        "scheme_category",
        "target_group",
        "created_at"
    )

    list_filter = ("category", "scheme_category", "target_group")
    search_fields = ("name", "ministry")

    inlines = [SchemeDocumentInline]

    fieldsets = (
        ("Basic Info", {
            "fields": ("name", "ministry", "description", "benefits")
        }),
        ("Classification", {
            "fields": ("category", "scheme_category", "target_group")
        }),
        ("Eligibility Rules", {
            "fields": ("eligibility_criteria",),
            "description": "Example: {'min_age':18,'max_income':200000,'requires_bpl':true}"
        }),
    )


@admin.register(SchemeDocument)
class SchemeDocumentAdmin(admin.ModelAdmin):
    list_display = ("name", "scheme", "is_required")
    list_filter = ("is_required",)
    search_fields = ("name",)
