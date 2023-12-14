from django.contrib import admin

from . models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("name",  "user", "status")
    list_filter= list_display

admin.site.register(Task, TaskAdmin)
