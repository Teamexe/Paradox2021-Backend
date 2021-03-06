# Generated by Django 3.1.6 on 2021-02-03 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='google_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='referral',
            old_name='google_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='paradoxuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
