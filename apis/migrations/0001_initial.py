# Generated by Django 3.1.6 on 2021-04-04 21:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExeGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=256)),
                ('type', models.CharField(choices=[('Video', 'Video'), ('Image', 'Image')], max_length=256)),
                ('credit', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ExeMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(limit_value=3, message='Name Length Should be greater than 3 charcters.')])),
                ('position', models.CharField(choices=[('Developer', 'Developer'), ('Mentor', 'Mentor'), ('Alumni', 'Alumni'), ('Final year', 'Final year'), ('Pre-Final year', 'Pre-Final year'), ('Coordinator', 'Coordinator'), ('Executive', 'Executive'), ('Volunteer', 'Volunteer')], max_length=255)),
                ('category', models.CharField(blank=True, choices=[('Full Stack', 'Full Stack'), ('Front End', 'Front End'), ('Back End', 'Back End'), ('Logo Designer', 'Logo Designer')], max_length=255, null=True)),
                ('image', models.URLField(max_length=255)),
                ('githubUrl', models.URLField(blank=True, max_length=255, null=True)),
                ('linkedInUrl', models.URLField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hints',
            fields=[
                ('level', models.IntegerField(primary_key=True, serialize=False)),
                ('hint1', models.CharField(max_length=255)),
                ('hint2', models.CharField(max_length=255)),
                ('hint3', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ParadoxUser',
            fields=[
                ('google_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(limit_value=3, message='Minimum Length should be 3 Characters')])),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('ref_code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('level', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], default='Easy', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='apis.paradoxuser', unique=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.URLField(max_length=255)),
                ('reg_time', models.DateTimeField(auto_now=True)),
                ('level', models.IntegerField(default=1)),
                ('attempts', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('coins', models.IntegerField(default=100)),
                ('super_coins', models.IntegerField(default=100)),
                ('refferral_availed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='apis.paradoxuser', unique=True)),
                ('ref_code', models.CharField(max_length=255, unique=True)),
                ('ref_success', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserHintLevel',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='apis.paradoxuser', unique=True)),
                ('level', models.IntegerField(default=1)),
                ('hintNumber', models.IntegerField(default=0)),
            ],
        ),
    ]
