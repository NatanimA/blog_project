# Generated by Django 3.2.5 on 2022-06-21 13:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comments_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 13, 51, 5, 273560, tzinfo=utc)),
        ),
    ]
