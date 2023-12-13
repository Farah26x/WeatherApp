import requests

def get_weather(city):
    API_key = "6d172d77ad6f201e6c7bb3d48604b814"
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        return "City not found"
    
    # Parsing the JSON response to get weather info
    weather_data = res.json()

    # Extracting data from the first item in the list
    current_weather = weather_data["list"][0]

    icon_id = current_weather["weather"][0]["icon"]
    temperature = current_weather["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
    description = current_weather["weather"][0]["description"]
    city = weather_data["city"]["name"]
    country = weather_data["city"]["country"]

    return (icon_id, temperature, description, city, country)

print(get_weather("London"))