# Generated by Django 2.2.4 on 2019-09-01 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='iamges/%Y/%m/%d'),
        ),
    ]