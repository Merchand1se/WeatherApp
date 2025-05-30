# Generated by Django 5.2.1 on 2025-05-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('temperature', models.FloatField(verbose_name='Температура (°C)')),
                ('feels_like', models.FloatField(verbose_name='Ощущается как (°C)')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('humidity', models.IntegerField(verbose_name='Влажность (%)')),
                ('pressure', models.IntegerField(verbose_name='Давление (hPa)')),
                ('wind_speed', models.FloatField(verbose_name='Скорость ветра (м/с)')),
                ('icon', models.CharField(max_length=10, verbose_name='Иконка погоды')),
                ('query_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата запроса')),
            ],
            options={
                'verbose_name': 'Запрос погоды',
                'verbose_name_plural': 'Запросы погоды',
                'ordering': ['-query_date'],
            },
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
