# Generated by Django 2.1.2 on 2019-04-13 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0009_exam_marks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks',
            name='subject',
        ),
        migrations.DeleteModel(
            name='marks',
        ),
    ]
