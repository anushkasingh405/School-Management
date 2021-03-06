# Generated by Django 2.1.2 on 2019-04-11 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended', models.IntegerField(default=0)),
                ('totalclasses', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entityname', models.CharField(max_length=200)),
                ('rollno', models.IntegerField(default=0)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='center.Departments')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='center.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=200)),
                ('entity', models.CharField(max_length=200)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='center.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='center.Course')),
            ],
        ),
        migrations.DeleteModel(
            name='Login1',
        ),
        migrations.AddField(
            model_name='course',
            name='Department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='center.Departments'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='rollno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='center.Entity'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='center.Subjects'),
        ),
    ]
