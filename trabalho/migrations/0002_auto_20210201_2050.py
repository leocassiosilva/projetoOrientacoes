# Generated by Django 3.1.5 on 2021-02-01 23:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trabalho', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabalho',
            name='id_usuario',
            field=models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
