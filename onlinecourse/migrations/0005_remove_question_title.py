# Generated by Django 3.1.3 on 2023-03-25 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0004_auto_20230325_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
    ]
