# Generated by Django 3.2 on 2021-05-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='date',
            field=models.DateField(null=True, verbose_name='Дата проведения занятия'),
        ),
    ]
