# courtesy of Instagram
# https://instagram.com/developer/endpoints/media/
import requests
import json
import os
from foo.utils import haversine, get_system_datetime_str, get_time_since

ACCESS_TOKEN = os.environ['INSTAGRAM_TOKEN']
BASEURL = "https://api.instagram.com/v1/media/search"
def get(latitude, longitude):
    resp = requests.get(BASEURL, params = { 'access_token': ACCESS_TOKEN,
        'lat': latitude, 'lng': longitude, 'count': 100})
    data = parse(resp.text, latitude = latitude, longitude = longitude)
    return data

def parse(txt, latitude, longitude):
    images = []
    data = json.loads(txt)
    for x in data['data']:
        d = {}
        d['url'] = x['link']
        d['likes'] = x['likes']['count']
        d['comments'] = x['comments']['count']
        d['caption'] = x['caption']['text'] if x['caption'] else ''
        d['image_url'] = x['images']['standard_resolution']['url']
        d['epoch'] = int(x['created_time'])
        d['filter'] = x['filter']
        d['username'] = x['user']['username']
        d['datetime_str'] = get_system_datetime_str(d['epoch'])
        d['time_since_now'] = get_time_since(d['epoch'])

        if x['location']:
            d['latitude'] = x['location']['latitude']
            d['longitude'] = x['location']['longitude']
            d['distance_from_reference'] = round(haversine(lat1 = latitude, lng1 = longitude,
                lat2 = d['latitude'], lng2 = d['longitude']), 1)

        images.append(d)

    return sorted(images, key = foo_pop, reverse = True)



def foo_pop(image):
    return image['likes'] + image['comments'] * 3
