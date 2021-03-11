# Generated by Django 3.1.7 on 2021-03-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20210310_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_schedule',
            name='end_time',
            field=models.TimeField(verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='class_schedule',
            name='periodicity',
            field=models.CharField(max_length=7, verbose_name='Частота'),
        ),
        migrations.AlterField(
            model_name='class_schedule',
            name='start_time',
            field=models.TimeField(verbose_name='Начало'),
        ),
        migrations.AlterField(
            model_name='class_schedule',
            name='week_day',
            field=models.CharField(max_length=31, verbose_name='День недели'),
        ),
    ]