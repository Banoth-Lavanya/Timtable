# Generated by Django 2.1.2 on 2018-12-08 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty_students',
            name='fid',
        ),
        migrations.RemoveField(
            model_name='faculty_students',
            name='student_id',
        ),
        migrations.DeleteModel(
            name='faculty_students',
        ),
    ]
