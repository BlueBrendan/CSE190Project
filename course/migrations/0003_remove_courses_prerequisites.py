# Generated by Django 3.2.9 on 2021-11-28 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20211128_0254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='prerequisites',
        ),
    ]
