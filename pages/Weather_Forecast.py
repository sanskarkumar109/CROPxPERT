import streamlit as st
import requests

# Coordinates from city name using Nominatim
def get_coordinates(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = response.json()
    if data:
        return float(data[0]["lat"]), float(data[0]["lon"])
    return None, None

# Weather from Open-Meteo
def get_weather(city):
    lat, lon = get_coordinates(city)
    if lat is None or lon is None:
        return None

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&daily=temperature_2m_max,temperature_2m_min,weathercode"
        f"&timezone=Asia%2FKolkata"
    )

    response = requests.get(weather_url)
    if response.status_code == 200:
        return response.json()
    return None

st.title("🌤️ 7-Day Weather Forecast")
city = st.text_input("Enter Indian City", "")

if city:
    weather_data = get_weather(city)

    if weather_data and "daily" in weather_data:
        st.write(f"**Weather Forecast for {city.capitalize()}**:")
        daily = weather_data["daily"]
        for i in range(len(daily["time"])):
            date = daily["time"][i]
            max_temp = daily["temperature_2m_max"][i]
            min_temp = daily["temperature_2m_min"][i]
            st.markdown(f"**📅 {date}**")
            st.markdown(f"🌡️ Max: {max_temp}°C | Min: {min_temp}°C")
            st.markdown("---")
    else:
        st.error("Could not retrieve weather info. Please check city name.")
