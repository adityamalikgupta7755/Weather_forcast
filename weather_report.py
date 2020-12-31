import requests
from datetime import datetime, timezone

# creat varables
url='http://api.openweathermap.org/data/2.5/weather?appid='
appid='fa127eb3c2c75223117a7ce9e5f9e4b2'
city=input("Enter your city name :-")

# concatinating all variables
f_url= url+appid+'&q='+city

# requesting server to give json data
data = requests.get(f_url).json()

# fetching useful data from data variable
data_coord_longitude = data['coord']['lon']
data_coord_latitude = data['coord']['lat']
data_weather_main = data['weather'][0]['main']
data_weather_description = data['weather'][0]['description']
# conver tempratuer from kelvi to celcius
data_temp = data['main']['temp']
data_temp = data_temp-273.15
data_temp = "{:.2f}".format(data_temp)

data_temp_min = data['main']['temp_min']
data_temp_min = data_temp_min-273.15
data_temp_min = "{:.2f}".format(data_temp_min)

data_temp_max = data['main']['temp_max']
data_temp_max = data_temp_max-273.15
data_temp_max = "{:.2f}".format(data_temp_max)

data_pressure = data['main']['pressure']
data_pressure_sea_level = data['main']['sea_level']
data_pressure_grnd_level = data['main']['grnd_level'] 
data_humidity = data['main']['humidity']

data_feels_like = data['main']['feels_like']
data_feels_like = data_feels_like-273.15
data_feels_like = "{:.2f}".format(data_feels_like)

data_visibility = (data['visibility'])/1000
data_wind_speed = data['wind']['speed']
data_wind_deg = data['wind']['deg']
c = data['clouds']["all"]

# 0 mean no visible cloud in the sky.
# few clouds: 11-25%
# scattered clouds: 25-50%
# broken clouds: 51-84%
# overcast clouds: 85-100%
data_clouds=""
if c>10 and c<25:
    data_clouds ="few clouds in the sky"
elif c>24 and c<51:
    data_clouds ="scattered clouds in the sky"
elif c>50 and c<85:
    data_clouds ="broken clouds in the sky"
elif c>84 and c<101:
    data_clouds ="overcast clouds in the sky"
else:
    data_clouds ="no visible cloud in the sky"
    
    
data_sys = data['sys']['country']
data_sys_sunrise = data['sys']['sunrise']
data_sys_sunset = data['sys']['sunset']
data_timezone = data['timezone']

data_name = data['name']

# print all desired data
print("-----------------------Area Details-----------------------------------------")
print("Coordinate are :-")
print("latitude :-",data_coord_latitude)
print("longitude :-",data_coord_longitude) 
print("Country :- ",data_sys) 
print("City :-",data_name) 
print("Time zone :-",datetime.utcfromtimestamp(data_timezone).strftime('%d-%m-%Y %H:%M:%S')) 
print("----------------------------------------------------------------")
print("---------------------Weather Report-----------------------------")
print("----------------------------------------------------------------")
print("Sunrise :-",datetime.utcfromtimestamp(data_sys_sunrise).strftime('%d-%m-%Y %H:%M:%S'))
print("Sunset :-",datetime.utcfromtimestamp(data_sys_sunset).strftime('%d-%m-%Y %H:%M:%S'))
print("Weather  :-",data_weather_main)
print("Weather Description :-",data_weather_description)
print("Temprature :-",data_temp,"°C")
print("Minmum Temprature :-",data_temp_min,"°C")
print("Maximum Temprature :-",data_temp_max,"°C")
print("Pressure :-",data_pressure,"hpa")
print("Pressure Sea Level:-",data_pressure_sea_level,"hpa")
print("Pressure Ground Level :-",data_pressure_grnd_level,"hpa")
print("Humidity :-",data_humidity,"%")
print("Feel Like :-",data_feels_like,"°C")
print("Visibility :-",data_visibility,"Km") 
print("Wind Speed :-",data_wind_speed,"km/h")
print("Wind degree :-",data_wind_deg,"°")
print("Cloud :- ",data_clouds) 
print("----------------------------------------------------------------")
