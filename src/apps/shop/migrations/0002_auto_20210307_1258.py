# Generated by Django 3.1.7 on 2021-03-07 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Количество'),
        ),
    ]