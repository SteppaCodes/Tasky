from django.db import models

#local imports
from apps.common.models import BaseModel
from apps.accounts.models import User
from .fields import OrderField, ParentTaskField
from . managers import FlowTaskManager

TASK_STATUS = (("not started", "not Started"),("completed", "completed"))

class Task(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=TASK_STATUS, default ="not started")

    def __str__(self):
        return self.name

class Flow(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="flows")
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name
   

class FlowTask(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    flow = models.ForeignKey(Flow, on_delete=models.CASCADE, related_name="flowtasks")
    order = FlowTaskManager.order_field
    old_order = models.IntegerField(null=True, blank=True)
    parent_task = ParentTaskField(blank=True, null=True, for_field=["flow"])

    def __str__(self):
        return self.task.name

    def save(self, *args, **Kwargs):
        if self.order is None:
            FlowTaskManager.calculate_order(self.flow)
            super().save(*args,**Kwargs)

        #FlowTaskManager.update_heirachy(self.flow, self.id)
        

        return super().save( *args, **Kwargs)
