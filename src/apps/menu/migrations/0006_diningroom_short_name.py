# Generated by Django 3.1.7 on 2021-03-23 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20210307_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='diningroom',
            name='short_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Короткое название'),
        ),
    ]