# Generated by Django 3.1.7 on 2021-03-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20210310_1357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam_schedule',
            options={'ordering': ['name'], 'verbose_name': 'Расписание экзамена', 'verbose_name_plural': 'Расписание экзаменов'},
        ),
        migrations.AlterModelOptions(
            name='subgroup',
            options={'ordering': ['number'], 'verbose_name': 'Подгруппа', 'verbose_name_plural': 'Подгруппы'},
        ),
        migrations.AddField(
            model_name='subgroup',
            name='number',
            field=models.PositiveIntegerField(default=1, max_length=1, verbose_name='Номер подгруппы'),
            preserve_default=False,
        ),
    ]
