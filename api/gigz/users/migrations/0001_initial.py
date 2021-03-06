# Generated by Django 2.2.2 on 2019-06-26 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GigzUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_lat', models.FloatField()),
                ('location_lng', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GigzEmployerUserProfile',
            fields=[
                ('gigzuserprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.GigzUserProfile')),
                ('posted_jobs', models.IntegerField()),
                ('employer_rating', models.FloatField()),
                ('employer_description', models.TextField()),
            ],
            bases=('users.gigzuserprofile',),
        ),
        migrations.CreateModel(
            name='GigzWorkerUserProfile',
            fields=[
                ('gigzuserprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.GigzUserProfile')),
                ('completed_jobs', models.IntegerField()),
                ('worker_rating', models.FloatField()),
                ('worker_description', models.TextField()),
            ],
            bases=('users.gigzuserprofile',),
        ),
    ]
