# Generated by Django 5.0.4 on 2024-04-09 17:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files_app', '0003_alter_encryptedfile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encryptedfile',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('71793576-3c82-4de8-8c76-2ed2ea0172e2'), editable=False, primary_key=True, serialize=False),
        ),
    ]
