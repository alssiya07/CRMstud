# Generated by Django 4.1.1 on 2022-11-25 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200, unique=True)),
                ('fees', models.PositiveIntegerField()),
                ('duration', models.CharField(max_length=500)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(null=True)),
                ('profile_Pic', models.ImageField(null=True, upload_to='image')),
                ('resume', models.FileField(null=True, upload_to='cvs')),
                ('qualification', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Placements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.students')),
            ],
        ),
        migrations.CreateModel(
            name='Batches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_code', models.CharField(max_length=200, unique=True)),
                ('started_date', models.DateField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.courses')),
            ],
        ),
        migrations.CreateModel(
            name='BatchStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.batches')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.students')),
            ],
            options={
                'unique_together': {('student', 'batch')},
            },
        ),
    ]