# Generated by Django 3.2.5 on 2022-06-21 15:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comments_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 15, 9, 17, 401943, tzinfo=utc)),
        ),
    ]
