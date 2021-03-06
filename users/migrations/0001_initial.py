# Generated by Django 4.0 on 2021-12-25 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics')),
                ('rollno', models.CharField(max_length=10)),
                ('year', models.CharField(choices=[('1', '1st'), ('2', '2nd'), ('3', '3rd'), ('4', '4th'), ('5', '5th')], default='1st', max_length=10)),
                ('branch', models.CharField(max_length=30)),
                ('techskills', models.TextField()),
                ('cv', models.FileField(blank=True, upload_to='resumes')),
                ('starred_projects', models.ManyToManyField(blank=True, related_name='starred_projects', to='home.Project')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
