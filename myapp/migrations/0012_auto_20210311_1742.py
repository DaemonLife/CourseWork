# Generated by Django 3.1.7 on 2021-03-11 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20210311_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='work_time',
        ),
        migrations.AddField(
            model_name='work_time',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.teacher'),
        ),
    ]