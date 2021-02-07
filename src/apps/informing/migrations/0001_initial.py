# Generated by Django 3.1.6 on 2021-02-07 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(editable=False, max_length=64, verbose_name='Автор')),
                ('text', models.TextField(verbose_name='Текст')),
                ('views', models.PositiveIntegerField(default=0, editable=False, verbose_name='Просмотры')),
                ('date_to', models.DateTimeField(verbose_name='Действует до')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Топик',
                'verbose_name_plural': 'Топики',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('information_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='informing.information')),
                ('name', models.CharField(max_length=512, verbose_name='Название')),
                ('logo', models.ImageField(upload_to='informing/events/', verbose_name='Афиша')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'ordering': ['-id'],
            },
            bases=('informing.information',),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('information_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='informing.information')),
                ('id_vk', models.PositiveIntegerField(default=0, editable=False, verbose_name='Номер записи в вк')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-id'],
            },
            bases=('informing.information',),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
                ('image', models.ImageField(blank=True, null=True, upload_to='informing/notification/', verbose_name='Изображение')),
                ('priority', models.PositiveIntegerField(choices=[(5, 'Нормальный'), (10, 'Высокий')], default=5, verbose_name='Приоритет')),
                ('message_id', models.TextField(editable=False)),
                ('topics', models.ManyToManyField(to='informing.Topic', verbose_name='Топики')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=36, verbose_name='Кто лайкнул')),
                ('information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informing.information')),
            ],
            options={
                'verbose_name': 'Лайк',
                'verbose_name_plural': 'Лайки',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='informing/news/', verbose_name='Изображение')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informing.news')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]