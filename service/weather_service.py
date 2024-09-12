from operator import itemgetter
from pkgutil import get_data

from toolz import first, pipe
from toolz.curried import partial, get_in

from api.weather_api import get_data
from utils.urls import get_weather_url
from models.weather import Wheathr


def get_weather(location):
    url = get_weather_url(location)
    weather = get_data(url)
    midnight_weather = get_midnight(weather)
    return Wheathr(
        get_in(["weather", 0, "main"], midnight_weather),
        get_in(["clouds", "all"], midnight_weather),
        get_in(["wind", "speed"], midnight_weather)
    )

def get_midnight(weather):
    return pipe(
        weather,
        itemgetter("list"),
        partial(filter, lambda x: "00:00:00" in x["dt_txt"]),
        first
    )

