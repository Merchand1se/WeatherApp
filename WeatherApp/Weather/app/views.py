from django.views import View
from django.views.generic import TemplateView
from .service import WeatherService
from .forms import CityForm
from django.http import HttpResponse
from django.shortcuts import render


class WeatherView(View):
    template_name = 'Weather.html'
    form_class = CityForm
    weather_service = WeatherService

    def get(self, request, *args, **kwargs):
        form = CityForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CityForm(request.POST)
        weather_data = None

        if form.is_valid():
            city_name = form.cleaned_data['city_name']
            weather_data = WeatherService.get_weather(city_name)

        return render(request, self.template_name, {
            'form': form,
            'weather_data': weather_data
        })

    def index(request):
        last_city = request.session.get("last_weather_city")

        if last_city:
            return render(request, "home.html", {"last_city": last_city})

        return HttpResponse("Добро пожаловать! Введите город для просмотра погоды.")

    def weather(request, city):
        request.session["last_weather_city"] = city
        return HttpResponse(f"Погода в {city}")

class Home(TemplateView):
    template_name = 'HomePage.html'