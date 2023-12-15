from django.contrib import admin

from . models import Task, Flow, FlowTask


class TaskAdmin(admin.ModelAdmin):
    list_display = ("name",  "user", "status")
    list_filter= list_display

class FlowAdmin(admin.ModelAdmin):
    list_display = ("name", "user")
    list_filter= list_display

class FlowTaskAdmin(admin.ModelAdmin):
    list_display = ("task", "flow", "created_at")
    list_filter= list_display


admin.site.register(Task, TaskAdmin)
admin.site.register(Flow, FlowAdmin)
admin.site.register(FlowTask, FlowTaskAdmin)
