# Generated by Django 4.2.6 on 2023-12-28 22:43

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
            field=models.UUIDField(default=uuid.UUID('0a20affb-d036-4ffc-a956-b934d077ad55'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]