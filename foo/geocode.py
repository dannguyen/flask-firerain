# courtesy of Google
# https://developers.google.com/maps/documentation/geocoding/
import requests
import json
BASEURL = "https://maps.googleapis.com/maps/api/geocode/json"
def get(addr):
    resp = requests.get(BASEURL, params = {'address': addr})
    data = parse(resp.text)
    return data

def parse(txt):
    """
    txt: raw text of a JSON response
    returns {"latitude": xxx, "longitude": yyy, "formatted_address": 'zzz'}
    """
    d = {'latitude': None, 'longitude': None, 'formatted_address': None}
    data = json.loads(txt)
    if data['results']:
        r = data['results'][0]
        d['latitude'] = r['geometry']['location']['lat']
        d['longitude'] = r['geometry']['location']['lng']
        d['formatted_address'] = r['formatted_address']

    return d
