# Generated by Django 3.1.5 on 2021-01-24 04:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_resume_vimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='navlogo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/logo'),
            preserve_default=False,
        ),
    ]
