
## Flask App Fire and Rain

A quickie <a href="http://flask.pocoo.org/">Python 3.x Flask app</a> that mashes data from Google Maps Geocoding, Instagram, Weather Underground, and the USGS Earthquake Hazards Program. A modification of [Ben Welsh's First News App with Flask](http://first-news-app.readthedocs.org/en/latest/). By <a href="https://twitter.com/dancow">Dan Nguyen</a> for <a href="http://www.compjour.org">CompJour</a>

It's called "Fire and Rain" but there's no wildfires API, so it's just earthquakes and weather and Instagram. It is also chock-full for horrible design decisions and spaghetti code and laughable test suite and it uses Python for what clearly should be front-end AJAX code.

It is currently deployed on [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python-o) at: [sleepy-mesa-7300.herokuapp.com/](http://sleepy-mesa-7300.herokuapp.com/)


## Setup

Basically, follow the steps outlined here: [Getting Started with Python on Heroku (devcenter.heroku.com)](https://devcenter.heroku.com/articles/getting-started-with-python-o) 

Once the app is created on Heroku, you have to add a couple of keys to the Heroku server:

~~~sh
heroku config:set WEATHER_UNDERGROUND_KEY=YOUR_WU_KEY
heroku config:set INSTAGRAM_TOKEN=YOUR_INSTAGRAM_KEY
~~~





