# Generated by Django 4.0 on 2022-05-08 05:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_profile_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='area_of_interest',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th')], default='Student', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='branch',
            field=models.CharField(choices=[('CSE', 'CSE'), ('DSE', 'DSE'), ('ME', 'ME'), ('EE', 'EE'), ('CE', 'CE'), ('BioE', 'BioE'), ('EP', 'EP')], default='none', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rollno',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th')], default='none', max_length=30),
        ),
    ]
