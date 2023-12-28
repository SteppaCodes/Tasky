from django.core.exceptions import ObjectDoesNotExist

from . fields import OrderField

class FlowTaskManager:
    order_field = OrderField(for_field=["flow"], blank=True)

    @classmethod
    def calculate_order(cls, flow):
        from .models import FlowTask

        try:
            last_item = FlowTask.objects.filter(flow=flow).order_by('-order').first()
        except ObjectDoesNotExist:
            last_item = None

        if last_item:
            order = cls.order_field.pre_save(last_item, True)
            return order
        else:
            return None

    # @classmethod
    # def update_heirachy(cls, flow, task_id):
    #     from . models import FlowTask
        
    #     tasks = FlowTask.objects.filter(flow=flow)
    #     task = FlowTask.objects.get(id = task_id)

    #     for task in tasks:
    #        task.old_order = task.order


    #     if task:
    #         print(task)
    #     else:
    #         print("sumn is wrong")
        


