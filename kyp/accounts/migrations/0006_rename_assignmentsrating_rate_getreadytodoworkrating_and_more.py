# Generated by Django 4.1 on 2023-02-06 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_timely_teacherrating_rate_timelyteacherrating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='assignmentsRating',
            new_name='getreadytodoworkRating',
        ),
        migrations.RenameField(
            model_name='rate',
            old_name='attendanceRating',
            new_name='skipclassyouwillnotpassRating',
        ),
    ]