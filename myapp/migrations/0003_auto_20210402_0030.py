# Generated by Django 3.1.1 on 2021-04-01 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_course_course_subject_offering_subject_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_subject',
            name='Course',
        ),
        migrations.RemoveField(
            model_name='course_subject',
            name='Subject_Code',
        ),
        migrations.RemoveField(
            model_name='offering',
            name='Subject_Code',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='T_Code',
        ),
        migrations.DeleteModel(
            name='COURSE',
        ),
        migrations.DeleteModel(
            name='COURSE_SUBJECT',
        ),
        migrations.DeleteModel(
            name='OFFERING',
        ),
        migrations.DeleteModel(
            name='SUBJECT',
        ),
        migrations.DeleteModel(
            name='TEACHER',
        ),
    ]
