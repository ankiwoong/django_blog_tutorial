# Generated by Django 3.0.6 on 2020-05-13 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogengine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=40, null=True, unique=True),
        ),
    ]
