# Generated by Django 3.0.6 on 2020-05-13 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogengine', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=1, max_length=40),
            preserve_default=False,
        ),
    ]