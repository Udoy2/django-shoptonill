# Generated by Django 3.1.7 on 2021-05-31 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupCommitte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60)),
                ('designation', models.CharField(max_length=60)),
                ('profile_pic', models.ImageField(upload_to='committe_profile_pic')),
            ],
        ),
    ]
