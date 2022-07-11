from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('result',)
    list_display = ('input', 'result')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Task, TaskAdmin)
