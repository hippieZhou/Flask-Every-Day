# Generated by Django 2.2.4 on 2019-09-01 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20190901_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletag',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to=settings.AUTH_USER_MODEL),
        ),
    ]