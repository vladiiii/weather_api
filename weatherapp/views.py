from django.shortcuts import render
import requests
import datetime as dt
import os


def index(request):
    # Geolocation
    y = get_ip(request)
    geo_url = requests.get(f"http://ip-api.com/json/{y}")
    geo_res = geo_url.json()
    lt = geo_res["lat"]
    lg = geo_res["lon"]

    # Weather
    appid = os.environ["KEY"]
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"lat": 56.3269, "lon": 44.0059, "appid": appid, "units": "metric"}
    r = requests.get(url=url, params=params)
    res = r.json()
    desc = res["weather"][0]["description"].title()
    temp = round(res["main"]["temp"])
    city_name = res["name"]

    day = dt.date.today().strftime("%b %d")
    return render(
        request,
        "weatherapp/index.html",
        {
            "desc": desc,
            "temp": temp,
            "city_name": city_name,
            "day": day,
        },
    )


def get_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return str(ip)
