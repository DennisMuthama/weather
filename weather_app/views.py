from django.shortcuts import render
from django.conf import settings
import requests


def index(request):
    api_key = settings.API_KEY
    city = 'Nakuru'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = response.json()

    weather = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }

    return render(request, 'weather_app/index.html', {'weather': weather})



