# Generated by Django 4.1 on 2022-09-13 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_avgrating_id_alter_avgrating_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avgrating',
            name='avgAssignmentsRating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='avgrating',
            name='avgAttendanceRating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='avgrating',
            name='avgClarityRating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='avgrating',
            name='avgTimingRating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
