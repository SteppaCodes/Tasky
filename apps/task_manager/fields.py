from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class OrderField(models.PositiveIntegerField):
    def __init__(self, for_field=None, *args, **Kwargs):
        self.for_field = for_field
        return super().__init__(*args, **Kwargs)

    def pre_save(self, model_instance, add):
        #self.attname is the name of the table that this custom field is used
        #self.model.objects.all() gets all objects in the model specifiedwhich is FlowTask
        #model_instance is the name of the model being saved
        if getattr(model_instance, self.attname) is None:
            try:
                if self.for_field:
                    qs = self.model.objects.all()
                    #Create a dictionay of the field that was specified in the model that is flow
                    query = {field:getattr(model_instance, field) for field in self.for_field}
                    #filter the model objects to only return objects with the field specified in the for_field
                    # The ** allows it to read the dictionary
                    qs = qs.filter(**query)
                last_item = qs.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)


class ParentTaskField(models.OneToOneField):
    def __init__(self, for_field=None, *args, **Kwargs):
        self.for_field = for_field
        Kwargs.setdefault("to", "Task")
        Kwargs.setdefault("on_delete", models.CASCADE)
        Kwargs.setdefault("related_name", "parent_tasks")

        return super().__init__(*args, **Kwargs)
    
    def pre_save(self, model_instance, add):
        
        if getattr(model_instance, self.attname) is None:
            try:
                if self.for_field:
                    qs = self.model.objects.all()
                    query = {field:getattr(model_instance, field) for field in self.for_field}
                    qs = qs.filter(**query)
                object_order = model_instance.order
                parent = qs.get(order=object_order-1)
                value = parent.task.id
                    
            except ObjectDoesNotExist:
                value = None
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)