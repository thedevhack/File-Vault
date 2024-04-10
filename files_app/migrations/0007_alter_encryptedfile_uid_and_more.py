# Generated by Django 5.0.4 on 2024-04-09 17:58

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files_app', '0006_alter_encryptedfile_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encryptedfile',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('7e29174a-4e67-4582-a944-651888a00de9'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='encryptedfile',
            name='uploaded_file',
            field=models.FileField(upload_to=''),
        ),
    ]
