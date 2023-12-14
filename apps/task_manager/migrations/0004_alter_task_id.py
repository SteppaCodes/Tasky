# Generated by Django 4.2.6 on 2023-12-14 19:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0003_alter_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
