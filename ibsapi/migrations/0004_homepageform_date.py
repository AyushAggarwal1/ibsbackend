# Generated by Django 4.2.13 on 2024-06-23 12:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ibsapi', '0003_alter_homepageform_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepageform',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]