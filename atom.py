import requests
import sys

# Weather function
def get_weather(city):
    api_key="af6adb4c6bb91f9afdbf5b2e09c9b7f4"
    url="https://api.openweathermap.org/data/2.5/weather"
    params={'q':city,'appid':api_key,'units':'metric'}

    response=requests.get(url,params=params)
    weather_data=response.json()    # Contains the result of response from the url

#   print(weather_data)   For checking the response to extract the essential
# get_weather("chennai")
    temp=weather_data["main"]["temp"]
    description=weather_data["weather"][0]['description']
    print(f"Temp of {city} is {temp} and condition is {description} ")
get_weather("chennai")

