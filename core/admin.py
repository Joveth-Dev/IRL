from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin as BaseGroupAdmin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from . import models


admin.site.unregister(Group)


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'user', 'section',
                    'action_flag', 'object_id', 'action']
    list_per_page = 10

    @admin.display(ordering='content_type')
    def section(self, logentry):
        return str(logentry.content_type).split(" | ")[-1]

    @admin.display(ordering='change_message')
    def action(self, logentry):
        return logentry

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.Account)
class AccountAdmin(BaseUserAdmin):
    list_display = ['username', 'email',
                    'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    # "is_superuser",
                    "groups",
                    # "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.Group)
class GroupAdmin(BaseGroupAdmin):
    list_per_page = 10
