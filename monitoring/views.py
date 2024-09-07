from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests

def index(request):
    return render(request, 'monitoring/index.html')

def air_view(request):
    # Example static data. Replace this with real API calls.
    location = "Your Area"
    aqi = 45
    aqi_condition = "Good"
    temperature = 22

    # For live data, use something like this:
    # response = requests.get('YOUR_API_URL')
    # data = response.json()
    # aqi = data['aqi']
    # temperature = data['temperature']

    context = {
        'location': location,
        'aqi': aqi,
        'aqi_condition': aqi_condition,
        'temperature': temperature,
    }

    return render(request, 'monitoring/air.html', context)

def noise_view(request):
    # Example static data. Replace this with real API calls or data retrieval.
    location = "Your Area"
    noise_level = 55  # Example noise level in dB
    noise_condition = "Moderate"

    # For live data, use something like this:
    # response = requests.get('YOUR_NOISE_API_URL')
    # data = response.json()
    # noise_level = data['noise_level']
    # noise_condition = data['noise_condition']

    context = {
        'location': location,
        'noise_level': noise_level,
        'noise_condition': noise_condition,
    }

    return render(request, 'monitoring/noise.html', context)