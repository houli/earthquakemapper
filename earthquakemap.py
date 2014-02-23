import json
import urllib2
import time
from earthquake import Earthquake
from flask import Flask, request, g, redirect, url_for, \
     abort, render_template

app = Flask(__name__)

data = json.load(urllib2.urlopen('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'))

length = len(data['features'])
earthquake_list = [None] * length

@app.before_request
def before_request():
    update_list()

@app.route('/')
def show_earthquakes():
    return render_template('show_earthquakes.html', earthquakes = earthquake_list)


def update_list():
    for i in range(0, length):
        identifier = i
        magnitude = data['features'][i]['properties']['mag']
        place = data['features'][i]['properties']['place']
        longitude = data['features'][i]['geometry']['coordinates'][0]
        latitude = data['features'][i]['geometry']['coordinates'][1]
        earthquake_time = data['features'][i]['properties']['time']
        depth = data['features'][i]['geometry']['coordinates'][2]
        new_earthquake = Earthquake(identifier, magnitude, place, longitude, latitude, earthquake_time, depth)
        earthquake_list[i] = new_earthquake


if __name__ == '__main__':
    app.run()