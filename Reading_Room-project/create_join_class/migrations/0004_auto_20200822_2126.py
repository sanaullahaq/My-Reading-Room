# Generated by Django 3.1 on 2020-08-22 15:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('create_join_class', '0003_classroom_classcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
