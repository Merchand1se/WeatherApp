from django.contrib import admin
from .models import WeatherQuery

@admin.register(WeatherQuery)
class WeatherQueryAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'temperature', 'query_date')
    list_filter = ('query_date', 'user')
    search_fields = ('city', 'description')