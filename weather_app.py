import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "2022f5ccd83b178b87047c36f09b788c"

def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            messagebox.showerror("Error", "City not found")
            return

        if response.status_code == 401:
            messagebox.showerror("Error", "Invalid API key")
            return

        response.raise_for_status()
        data = response.json()

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        result_label.config(
            text=f"City: {city.title()}\n"
                 f"Temperature: {temperature}°C\n"
                 f"Feels Like: {feels_like}°C\n"
                 f"Humidity: {humidity}%\n"
                 f"Weather: {description.title()}\n"
                 f"Wind Speed: {wind_speed} m/s"
        )

    except requests.exceptions.Timeout:
        messagebox.showerror("Error", "Network timeout")

    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Network error")


# GUI window
window = tk.Tk()
window.title("Weather App")
window.geometry("400x400")

title_label = tk.Label(
    window,
    text="Weather App",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=20)

city_entry = tk.Entry(window, width=30, font=("Arial", 14))
city_entry.pack(pady=10)

get_button = tk.Button(
    window,
    text="Get Weather",
    command=get_weather,
    font=("Arial", 12)
)
get_button.pack(pady=10)

result_label = tk.Label(
    window,
    text="Enter a city to see weather",
    font=("Arial", 12),
    justify="left"
)
result_label.pack(pady=20)

window.mainloop()