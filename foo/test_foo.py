import json
from foo.geocode import parse as parse_geo
from foo.quakes import parse as parse_quakes
from foo.images import parse as parse_images
from foo.weather import parse as parse_weather
from foo.weather import parse_satellite as parse_weather_satellite
TEST_LAT = 37.42826410
TEST_LNG = -122.1688453

def get_geo(addr="whatever this is ignored"):
    with open('./static/test_foo/geocode_data.json') as f:
        return parse_geo(f.read())

def get_quakes(latitude='ignored', longitude = 'ignored'):
    with open('./static/test_foo/quakes_data.json') as f:
        return parse_quakes(f.read(), latitude = TEST_LAT, longitude = TEST_LNG)


def get_weather(latitude='ignored', longitude = 'ignored'):
    with open('./static/test_foo/weather_data.json') as f:
        d = parse_weather(f.read())
    with open('./static/test_foo/weather_satellite.json') as g:
        d.update(parse_weather_satellite(g.read()))
    return d


def get_images(latitude='ignored', longitude = 'ignored'):
    with open('./static/test_foo/images_data.json') as f:
        return parse_images(f.read(), latitude = TEST_LAT, longitude = TEST_LNG)

