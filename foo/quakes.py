# courtesy of USGS
# http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
from datetime import datetime
from operator import itemgetter
import requests
import json
from foo.utils import haversine, get_system_datetime_str, get_time_since
from copy import deepcopy
BASEURL = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson'
def get(url = BASEURL, lat = None, lng = None):
    resp = requests.get(url)
    quakes = parse(resp.text, lat = lat, lng = lng)
    return quakes



def parse(txt, lat, lng):
    """
    returns:
        [
            {
                'magnitude': 9.0,
                'url': "http:zzz",
                'place': 'xyz',
                'time': 15200020202,
                'latitude': 30.0,
                'longitude': 40
            }
        ]
    """
    quakes = []
    data = json.loads(txt)
    for q in data['features']:
        x = {
            'magnitude': q['properties']['mag'],
            'url': q['properties']['url'],
            'place': q['properties']['place'],
            'latitude': q['geometry']['coordinates'][1],
            'longitude': q['geometry']['coordinates'][0]
        }
        x['epoch'] = q['properties']['time'] / 1000
        x['datetime_str'] = get_system_datetime_str(x['epoch'])
        x['time_since_now'] = get_time_since(x['epoch'])

        x['distance_from_reference'] = round(haversine(lat1 = lat, lng1 = lng , lat2 = x['latitude'], lng2 = x['longitude']))
        quakes.append(x)

    return sorted(quakes, key = itemgetter('distance_from_reference'))



