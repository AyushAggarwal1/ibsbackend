# Generated by Django 4.2.13 on 2024-06-23 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ibsapi', '0006_remove_homepageform_date_remove_homepageform_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepageform',
            name='datetime',
        ),
        migrations.AddField(
            model_name='homepageform',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepageform',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
