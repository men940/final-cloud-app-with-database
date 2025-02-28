# Generated by Django 3.1.3 on 2023-03-25 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_auto_20230325_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='question text', max_length=550),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(default='question title', max_length=550),
        ),
    ]
