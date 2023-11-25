import requests as r
import json
def weather_prognose(city):
    API_key="Here you should write your API_key from https://home.openweathermap.org/api_keys "
    f=f'https://api.openweathermap.org/data/2.5/weather?&q={city}&lang=ru&units=metric&appid={API_key}'
    weather=r.get(f).json()
    temp=round(weather['main']['temp'])
    sky=(weather['weather'][0]['description'])
    wind_deg=round(weather['wind']['deg'])
    humidity = weather['main']['humidity']
    if 45<wind_deg<=135:
        wd='Восточный'
    if 135<wind_deg<=225:
        wd='Южный'
    if 225<wind_deg<=315:
        wd='Западный'
    if 315<=wind_deg or wind_deg<=45:
        wd='Северный'
    wind_speed=(weather['wind']['speed'])
    print(f'Сейчас {sky}')
    print(f'Температура: {temp}С')
    print(f'Направление ветра: {wind_deg}({wd} ветер)')
    print(f'Скорость ветра: {wind_speed}')
    print(f'Влажность {humidity}%')

weather_prognose(input('В каком городе вам показать погоду?'))