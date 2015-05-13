from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from urllib.parse import quote_plus, unquote_plus

import json
from foo.geocode import get as get_geo
from foo.quakes import get as get_quakes
from foo.weather import get as get_weather
from foo.images import get as get_images



app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/go", methods=['POST'])
def go():
    address = request.form.get('address')
    print(address)
    fixed_path = quote_plus(address)
    return redirect("/address/%s" % fixed_path)

@app.route('/address/<addr>/')
def results(addr):
    addr_orig = unquote_plus(addr)
    geo = get_geo(addr_orig)
    lat = geo['latitude']
    lng = geo['longitude']
    full_address = geo['formatted_address']
    return render_template('results.html',
        latitude = lat,
        longitude = lng,
        address_searched = addr_orig,
        full_address = full_address,
        short_address = ', '.join(full_address.split(',')[0:2]),
        quakes = get_quakes(latitude = lat, longitude = lng),
        weather = get_weather(latitude = lat, longitude = lng),
        images = get_images(latitude = lat, longitude = lng),
        geo = geo
    )

    return render_template('results.html', address = addr_readable)


@app.route('/test/<addr>/')
def test_page(addr):
    from foo import test_foo
    addr_orig = unquote_plus(addr)
    geo = test_foo.get_geo(addr_orig)
    lat = geo['latitude']
    lng = geo['longitude']
    full_address = geo['formatted_address']
    return render_template('results.html',
        latitude = lat,
        longitude = lng,
        address_searched = addr_orig,
        full_address = full_address,
        short_address = ', '.join(full_address.split(',')[0:2]),
        quakes = test_foo.get_quakes(latitude = lat, longitude = lng),
        weather = test_foo.get_weather(latitude = lat, longitude = lng),
        images = test_foo.get_images(latitude = lat, longitude = lng),
        geo = geo
    )

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)
