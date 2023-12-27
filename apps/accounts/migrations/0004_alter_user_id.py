# Generated by Django 4.2.6 on 2023-12-27 15:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d0de2e7e-8385-465f-99fa-7d0bd27c5945'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
