# Generated by Django 4.0 on 2022-03-10 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_remove_project_mailnotification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='DatePosted',
            field=models.DateTimeField(default=datetime.date(2022, 3, 10)),
        ),
        migrations.AlterField(
            model_name='project',
            name='Duration',
            field=models.CharField(choices=[('<1 month', '< 1 month'), ('1-2 months', '1-2 months'), ('2-4 months', '2-4 months'), ('4-6 months', '4-6 months'), ('6-12 months', '6-12 months'), ('>12 months', '> 12 months')], max_length=30),
        ),
    ]