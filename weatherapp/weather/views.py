from django.shortcuts import render
from .models import City
 
from .forms import CityForm
import requests
import json
#  user key : APIkey=b77e07f479efe92156376a8b07640ced

def weather(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=b77e07f479efe92156376a8b07640ced'
    if request.method =='POST':
        form=CityForm(request.POST)
        form.save()
   
    form=CityForm()
    cities = City.objects.all()
    for city in cities:
        rep=requests.get(url.format(city)).json()
        city_weather={
        'city':city.name,
        #converting temperature from kelvin to celsius than printing the float number with 2 decimal places ,
        'temperature':"{:.2f}".format((rep['main']['temp']-273.15)),
        'wind_speed':rep['wind']['speed'],
        'description':rep['weather'][0]['description'],
        'humidity':rep['main']['humidity'],
        'icon':rep['weather'][0]['icon'],
        }
        #print(city_weather)
    context={
        'city_weather':city_weather,
        'form':form
    }
    return render(request,'index.html',context=context)




