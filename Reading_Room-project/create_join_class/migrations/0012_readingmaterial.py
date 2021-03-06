# Generated by Django 3.1 on 2020-09-06 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('create_join_class', '0011_delete_readingmaterial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('readingFile', models.FileField(upload_to='uploads/ReadingMaterial/')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom', to='create_join_class.classroom')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
