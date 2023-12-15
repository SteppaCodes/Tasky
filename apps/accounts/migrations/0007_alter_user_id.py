# Generated by Django 4.2.6 on 2023-12-14 20:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('86026111-1a93-4370-b10a-16f602d8bde2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
