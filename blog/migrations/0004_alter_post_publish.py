# Generated by Django 5.0.1 on 2024-02-08 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 15, 39, 27, 94534, tzinfo=datetime.timezone.utc)),
        ),
    ]
