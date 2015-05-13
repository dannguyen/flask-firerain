import json
from foo.geocode import parse as parse_geo
from foo.quakes import parse as parse_quakes
from foo.weather import parse as parse_weather
from foo.weather import parse_satellite as parse_weather_satellite
# from weather import parse_image as parse_weather_image


def get_geo():
    with open('./static/test_foo/geocode_data.json') as f:
        return parse_geo(f.read())

def get_quakes():
    with open('./static/test_foo/quakes_data.json') as f:
        return parse_quakes(f.read(), lat = 37.42826410, lng = -122.1688453)


def get_weather():
    with open('./static/test_foo/weather_data.json') as f:
        d = parse_weather(f.read())
    with open('./static/test_foo/weather_satellite.json') as g:
        d.update(parse_weather_satellite(g.read()))
    return d



