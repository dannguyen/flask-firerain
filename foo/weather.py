# courtesy of Weather Underground's API
# http://www.wunderground.com/weather/api/d/docs?d=index
import requests
import json
import os
from datetime import datetime
from foo.utils import get_system_datetime_str, get_time_since
BASEURL = 'http://api.wunderground.com/api/{key}/conditions/q/{latitude},{longitude}.json'
SAT_BASEURL = 'http://api.wunderground.com/api/{key}/satellite/q/{latitude},{longitude}.json'
WEATHERKEY = os.environ['WEATHER_UNDERGROUND_KEY']
def get(latitude, longitude):
    atts = {'latitude': latitude, 'longitude': longitude, 'key': WEATHERKEY}
    resp = requests.get(BASEURL.format(**atts))
    data = parse(resp.text)
    sat_resp = requests.get(SAT_BASEURL.format(**atts))
    sat_data = parse_satellite(sat_resp.text)
    data.update(sat_data)
    return data


def parse(txt):
    """
    returns:
    {
        'observation_location': 'Springfield, USA',
        'datetime_str': '5:00PM (Pacific Time), January 20, 1920',

        etc
    }
    """
    data = json.loads(txt)
    d = {}
    obs = data.get('current_observation')
    if obs:
        d['observation_location'] = obs['observation_location']['full']
        d['epoch'] = int(obs['observation_epoch'])
        d['datetime_str'] = get_system_datetime_str(d['epoch'])
        d['time_since_now'] = get_time_since(d['epoch'])
        d['description'] = obs['weather']
        d['icon_url'] = obs['icon_url']
        d['url'] = obs['ob_url']
        d['temp'] = obs['temp_f']
        d['feels_like_temp'] = obs['feelslike_f']
        d['relative_humidity'] = obs['relative_humidity']
        d['wind_speed'] = obs['wind_mph']
    return d


def parse_satellite(txt):
    """
    returns: {
        satellite: http://url.jpg
    }
    """
    data = json.loads(txt)
    d = {'satellite_image_url': 'http://zzz.com/i.jpg'}
    sat = data.get('satellite')
    if sat:
        d['satellite_image_url'] = sat['image_url'].replace(WEATHERKEY, 'ZZZ')
    return d
