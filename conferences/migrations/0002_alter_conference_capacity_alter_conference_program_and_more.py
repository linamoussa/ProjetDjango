# Generated by Django 4.2 on 2024-10-17 20:59

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='capacity',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=900, message='capacity must be under 900')]),
        ),
        migrations.AlterField(
            model_name='conference',
            name='program',
            field=models.FileField(upload_to='files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpeg', 'jpg'], message="Only 'pdf', 'png', 'jpeg', 'jpg' are allowed.")]),
        ),
        migrations.AddConstraint(
            model_name='conference',
            constraint=models.CheckConstraint(check=models.Q(('start_date__gte', datetime.date(2024, 10, 17))), name='the start date must be grater or equal than today'),
        ),
    ]
