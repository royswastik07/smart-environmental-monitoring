from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests

def index(request):
    return render(request, 'monitoring/index.html')

def air(request):
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

    return render(request, 'air.html', context)