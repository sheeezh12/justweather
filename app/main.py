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
    url = "http://www.geoplugin.net/extras/location.gp"
    param = {
        "name" : city,
        "format" : "json"
    }
    res = requests.get(url, params=param, timeout=5).json()
    lat = res.get("geoplugin_latitude")
    lon = res.get("geoplugin_longitude")
    return lat, lon

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

    lat, lon = get_coord(city)
    if lat and lon:
        data = get_forecast(lat, lon)
        daily = data.get("daily", {})
        timezone = data.get("timezone", "Asia/Jakarta")
        return render_template("base.html", city=city, data=daily, timezone=timezone)
    else:
        error = f"Kota '{city}' tidak ditemukan."
        return render_template("base.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)