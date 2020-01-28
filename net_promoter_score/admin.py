from django.contrib import admin

from .models import UserScore


class UserScoreAdmin(admin.ModelAdmin):
    """Admin model for UserScore objects."""

    list_display = ("user", "timestamp", "score", "group", "source")
    list_filter = ("timestamp", "group", "source")
    readonly_fields = ("user", "timestamp", "score", "group", "reason")


admin.site.register(UserScore, UserScoreAdmin)
