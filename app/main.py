from flask import Flask, render_template, request
import os
import requests
import re
from markupsafe import escape


app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'template'),
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'static')
)
def is_valid_city(city):
    city = city.strip()
    return bool(re.match(r"^[a-zA-Z\s\-]{1,40}$", city))

def get_coord(city):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city,
        "format": "json",
        "limit": 1,
        "addressdetails": 1,
        "accept-language": "id"
    }
    headers = {
        "User-Agent": "JustWeather v1.0"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()

        if not data:
            return None, None, None

        loc = data[0]
        lat = float(loc["lat"])
        lon = float(loc["lon"])
        display_name = loc.get("display_name", "")
        place_type = loc.get("type", "")

        if place_type not in ["city", "town", "village", "municipality", "administrative"]:
            return None, None, None

        return lat, lon, display_name

    except (requests.RequestException, ValueError, IndexError):
        return None, None, None

def get_forecast(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,weathercode",
        "timezone": "Asia/Jakarta"
    }
    resp = requests.get(url, params=params).json()
    return resp

WEATHER_CODES = {
    0: "Cerah",
    1: "Sebagian cerah",
    2: "Sebagian berawan",
    3: "Berawan penuh",
    45: "Berkabut",
    48: "Berkabut (embun beku)",
    51: "Gerimis ringan",
    53: "Gerimis sedang",
    55: "Gerimis lebat",
    61: "Hujan ringan",
    63: "Hujan sedang",
    65: "Hujan deras",
    80: "Hujan lokal",
    81: "Hujan lokal sedang",
    82: "Hujan lokal deras",
    95: "Badai petir",
    96: "Badai petir + hujan es ringan",
    99: "Badai petir + hujan es deras"
}

def get_weather_description(code):
    return WEATHER_CODES.get(int(code), "Tidak diketahui")



@app.route("/")
def main():
    return render_template("base.html")

@app.route("/forecast", methods=["POST"])
def forecast():
    raw_city = request.form.get("city", "")
    city = escape(raw_city.strip())

    if not is_valid_city(city):
        error = "Nama kota tidak valid."
        return render_template("base.html", error=error)

    lat, lon, display_name = get_coord(city)
    if lat is None or lon is None:
        error = f"Kota '{city}' tidak ditemukan."
        return render_template("base.html", error=error)

    data = get_forecast(lat, lon)
    if not data:
        error = "Gagal mengambil data cuaca. Silakan coba lagi."
        return render_template("base.html", error=error)

    daily = data.get("daily", {})
    timezone = data.get("timezone", "Asia/Jakarta")

    return render_template("base.html", city=city, data=daily, timezone=timezone, display_name=display_name, get_weather_description=get_weather_description
)

if __name__ == "__main__":
    app.run(debug=True)