# Prints weather location from CMD Line
import json, requests, sys
from pprint import pprint

# Set Location
DEFAULT_LOCATION = 'Rossmoor, CA'
location = DEFAULT_LOCATION if len(sys.argv) < 2 else ' '.join(sys.argv[1:])

# Download JSON Data from OpenWeatherMap.org API
API_KEY = '4e622e995a5d6e62d2118933697414e7'
open_weather_map_api_url = f'http://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3&APPID={API_KEY}'
print(open_weather_map_api_url)
response = requests.get(open_weather_map_api_url)
response.raise_for_status() # Check for error

weatherData = json.loads(response.text)
pprint(weatherData)
weather = weatherData['list']

print(f"""
Current weather in {location} is: {weather[0]['weather'][0]['main']} - {weather[0]['weather'][0]['description']}
Tomorrow: {weather[1]['weather'][0]['main']} - {weather[1]['weather'][0]['description']}
Day after Tomorrow: {weather[2]['weather'][0]['main']} - {weather[2]['weather'][0]['description']}
""")