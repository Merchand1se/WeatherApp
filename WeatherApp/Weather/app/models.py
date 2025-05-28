from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class WeatherQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Пользователь")
    city = models.CharField(max_length=100, verbose_name="Город")
    temperature = models.FloatField(verbose_name="Температура (°C)")
    feels_like = models.FloatField(verbose_name="Ощущается как (°C)")
    description = models.CharField(max_length=200, verbose_name="Описание")
    humidity = models.IntegerField(verbose_name="Влажность (%)")
    pressure = models.IntegerField(verbose_name="Давление (hPa)")
    wind_speed = models.FloatField(verbose_name="Скорость ветра (м/с)")
    icon = models.CharField(max_length=10, verbose_name="Иконка погоды")
    query_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата запроса")

    class Meta:
        verbose_name = "Запрос погоды"
        verbose_name_plural = "Запросы погоды"
        ordering = ['-query_date']

    def __str__(self):
        return f"{self.city} - {self.query_date}"