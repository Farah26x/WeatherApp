import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

# Function to get weather from openweathermap API
def get_weather(city):
    API_key = "6d172d77ad6f201e6c7bb3d48604b814"
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    # Parsing the JSON response to get weather info
    weather = res.json()

    # Extracting data from the first item in the list
    current_weather = weather["list"][0]

    icon_id = current_weather["weather"][0]["icon"]
    temperature = current_weather["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
    description = current_weather["weather"][0]["description"]
    city = weather["city"]["name"]
    country = weather["city"]["country"]

    # Getting the image for the corresponding icon id
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

# Function to search the weather
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    # if city found unpack weather info
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    # get weather icon
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    #Update the temp and desc labels
    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")

root = ttkbootstrap.Window(themename="darkly")
root.title("Weather app")
root.geometry("400x400")

# Widget to enter the city name
city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

# Button to search for weather information
search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

# Labels showing city and country name
location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

# Image showing the weather icon
icon_label = tk.Label(root)
icon_label.pack()

# Widget showing the temperature
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

# Widget showing the current weather description
description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

root.mainloop()