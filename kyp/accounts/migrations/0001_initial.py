# Generated by Django 4.1 on 2022-09-11 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=10)),
                ('rating', models.FloatField(blank=True, default=None, null=True)),
                ('post', models.CharField(max_length=20)),
                ('pic', models.ImageField(upload_to='')),
                ('email', models.EmailField(max_length=254)),
                ('ph_num', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_rating', models.FloatField(blank=True, default=None, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='accounts.profile')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='accounts.tag')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='tag',
            field=models.ManyToManyField(to='accounts.tag'),
        ),
        migrations.CreateModel(
            name='AvgRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_avgRating', models.FloatField(blank=True, default=None, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avg_profile', to='accounts.profile')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avg_tag', to='accounts.tag')),
            ],
            options={
                'unique_together': {('tag', 'profile')},
            },
        ),
    ]
