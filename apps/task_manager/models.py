from django.db import models

#local imports
from apps.common.models import BaseModel
from apps.accounts.models import User

TASK_STATUS = (("not started", "not Started"),("completed", "completed"))

class Task(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=TASK_STATUS, default ="not started")

    def __str__(self):
        return self.name

