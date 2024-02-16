# Generated by Django 4.2 on 2024-02-15 23:23

import account.utils.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_freelancer', models.BooleanField(default=False)),
                ('headline', models.CharField(blank=True, max_length=60, validators=[account.utils.validators.validate_first_letter], verbose_name='Headline')),
                ('bio', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[account.utils.validators.validate_phone], verbose_name='Phone Number')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=60, verbose_name='Competence Name')),
            ],
            options={
                'verbose_name': 'Competence',
                'verbose_name_plural': 'Competences',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100, validators=[account.utils.validators.validate_first_letter, account.utils.validators.validate_safe_text], verbose_name='Job Title')),
                ('company', models.CharField(max_length=70, validators=[account.utils.validators.validate_safe_text], verbose_name='Company')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, verbose_name='End Date')),
                ('job_type', models.CharField(choices=[('TR', 'Trainee'), ('IN', 'Internship'), ('FT', 'Full-time'), ('PT', 'Part-time'), ('FL', 'Free lance'), ('AU', 'Autonomous'), ('AP', 'Apprentice'), ('TP', 'Third Party')], default='FT', max_length=2, verbose_name='Job Type')),
                ('competences', models.ManyToManyField(blank=True, related_name='jobs', to='account.competence', verbose_name='Competences')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='EducationalBackground',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('institution', models.CharField(max_length=70, validators=[account.utils.validators.validate_first_letter, account.utils.validators.validate_safe_text], verbose_name='Institution')),
                ('degree', models.CharField(max_length=50, validators=[account.utils.validators.validate_first_letter, account.utils.validators.validate_safe_text], verbose_name='Degree')),
                ('field_of_study', models.CharField(max_length=50, validators=[account.utils.validators.validate_first_letter, account.utils.validators.validate_safe_text], verbose_name='Field of Study')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, verbose_name='End Date')),
                ('competences', models.ManyToManyField(blank=True, related_name='educational_backgrounds', to='account.competence', verbose_name='Competences')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educational_backgrounds', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Educational Background',
                'verbose_name_plural': 'Educational Backgrounds',
            },
        ),
    ]
