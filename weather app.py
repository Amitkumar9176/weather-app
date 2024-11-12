import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
app = tk.Tk()
app.title("Weather App")
app.geometry("350x400")
app.config(bg="#87CEEB")

# Function to simulate fetching weather data
# (Replace this with actual API calls in the future)
def get_weather():
    city = city_entry.get()
    if city:
        # Simulate weather data for demonstration purposes
        temperature = "25°C"
        description = "Clear Sky"
        humidity = "60%"
        
        temp_label.config(text=f"Temperature: {temperature}")
        desc_label.config(text=f"Description: {description}")
        humidity_label.config(text=f"Humidity: {humidity}")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

# UI Elements

# Title Label
title_label = tk.Label(app, text="Weather App", font=("Arial", 18, "bold"), bg="#87CEEB", fg="white")
title_label.pack(pady=10)

# City Entry Field
city_label = tk.Label(app, text="Enter city name:", font=("Arial", 12), bg="#87CEEB", fg="white")
city_label.pack(pady=5)
city_entry = tk.Entry(app, font=("Arial", 14), width=20)
city_entry.pack(pady=5)

# Search Button
search_button = tk.Button(app, text="Search", font=("Arial", 12), bg="#4CAF50", fg="white", width=12, command=get_weather)
search_button.pack(pady=10)

# Weather Information Display
temp_label = tk.Label(app, text="Temperature: --", font=("Arial", 12), bg="#87CEEB", fg="white")
temp_label.pack(pady=5)
desc_label = tk.Label(app, text="Description: --", font=("Arial", 12), bg="#87CEEB", fg="white")
desc_label.pack(pady=5)
humidity_label = tk.Label(app, text="Humidity: --", font=("Arial", 12), bg="#87CEEB", fg="white")
humidity_label.pack(pady=5)

# Run the application
app.mainloop()