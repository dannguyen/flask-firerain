from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from urllib.parse import quote_plus, unquote_plus

import json
from foo.geocode import get as get_geo
from foo.quakes import get as get_quakes
from foo.weather import get as get_weather



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
    return render_template('results.html',
        latitude = geo['latitude'],
        longitude = geo['longitude'],
        address_searched = addr_orig,
        quakes = get_quakes(lat = geo['latitude'], lng = geo['longitude']),
        weather = get_weather(geo),
        geo = geo
    )

    return render_template('results.html', address = addr_readable)


@app.route('/test/<addr>/')
def test_page(addr):
    from foo import test_foo
    addr_orig = unquote_plus(addr) + ' [TEST]'
    geo = test_foo.get_geo()
    return render_template('results.html',
        latitude = geo['latitude'],
        longitude = geo['longitude'],
        address_searched = addr_orig,
        quakes = test_foo.get_quakes(),
        weather = test_foo.get_weather(),
        geo = geo
    )

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)
