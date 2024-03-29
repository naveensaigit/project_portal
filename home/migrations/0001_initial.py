# Generated by Django 4.1.7 on 2023-03-24 13:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Image', models.ImageField(blank=True, default='images.jpeg', upload_to='project_pics', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])),
                ('Description', models.TextField()),
                ('Status', models.CharField(choices=[('Open', 'Open'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed')], default='Open', max_length=10)),
                ('OpenedFor', models.CharField(max_length=2000)),
                ('Difficulty', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Hard', 'Hard')], default='Beginner', max_length=15)),
                ('DesiredQualifications', models.TextField()),
                ('Duration', models.CharField(choices=[('<1 month', '< 1 month'), ('1-2 months', '1-2 months'), ('2-4 months', '2-4 months'), ('4-6 months', '4-6 months'), ('6-12 months', '6-12 months'), ('>12 months', '> 12 months')], max_length=30)),
                ('DatePosted', models.DateTimeField(default=django.utils.timezone.now)),
                ('SelectionCriteria', models.TextField()),
                ('Question', models.TextField()),
                ('Likes', models.IntegerField(default=0)),
                ('AlreadyApplied', models.ManyToManyField(blank=True, related_name='AlreadyApplied', to=settings.AUTH_USER_MODEL)),
                ('FloatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FloatedBy', to=settings.AUTH_USER_MODEL)),
                ('Mentors', models.ManyToManyField(related_name='Mentors', to=settings.AUTH_USER_MODEL)),
                ('Tags', models.ManyToManyField(related_name='Tags', to='home.tag')),
            ],
        ),
        migrations.CreateModel(
            name='ApplyRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.TextField()),
                ('Status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], max_length=10)),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.project')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
