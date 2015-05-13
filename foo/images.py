# courtesy of Instagram
# https://instagram.com/developer/endpoints/media/
import requests
import json
import os
ACCESS_TOKEN = os.environ['INSTAGRAM_TOKEN']
BASEURL = "https://api.instagram.com/v1/media/search"
def get(latitude, longitude):
    resp = requests.get(BASEURL, params = { 'access_token': ACCESS_TOKEN,
        'lat': latitude, 'lng': longitude, 'count': 100})
    data = parse(resp.text)
    return data

def parse(txt):
    images = []
    data = json.loads(txt)
    for x in data['data']:
        d = {}
        d['url'] = x['link']
        d['likes'] = x['likes']['count']
        d['comments'] = x['comments']['count']
        d['caption'] = x['caption']['text'] if x['caption'] else ''
        d['image_url'] = x['images']['standard_resolution']['url']
        d['epoch'] = x['created_time']
        d['filter'] = x['filter']
        d['username'] = x['user']['username']
        if x['location']:
            d['latitude'] = x['location']['latitude']
            d['longitude'] = x['location']['longitude']
        images.append(d)

    return sorted(images, key = foo_pop, reverse = True)



def foo_pop(image):
    return image['likes'] + image['comments'] * 3
