from django.contrib import admin
from django import forms

from .models import (
    Post,
    Order,
    Technology,
    Project,
    ContactMessage,
)


# =========================
# POST
# =========================

admin.site.register(Post)


# =========================
# ORDER
# =========================

class OrderAdminForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = "__all__"

        widgets = {
            "status": forms.Select(
                choices=Order.STATUS_CHOICES
            ),
        }


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    form = OrderAdminForm

    list_display = (
        "id",
        "user",
        "name",
        "phone",
        "service",
        "price",
        "status",
        "created_at",
    )

    list_display_links = (
        "id",
    )

    list_filter = (
        "status",
        "service",
        "created_at",
    )

    search_fields = (
        "user__username",
        "name",
        "phone",
    )


# =========================
# TECHNOLOGY
# =========================

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
    )

    search_fields = (
        "name",
    )


# =========================
# PROJECT
# =========================

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "created_at",
    )

    search_fields = (
        "name",
        "description",
    )

    filter_horizontal = (
        "technologies",
    )


# =========================
# CONTACT MESSAGE
# =========================

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "created_at",
    )

    list_filter = (
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "message",
    )

    readonly_fields = (
        "created_at",
    )