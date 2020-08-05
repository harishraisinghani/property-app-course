from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from realtorapi import get_realtor_data, get_csv_data, set_markers
from scraper import coastcapital
from flask_googlemaps import GoogleMaps, Map

app = Flask(__name__)


app.config['GOOGLEMAPS_KEY'] = "AIzaSyBgk4xlA90gmaW-itRDlPgokqU5SgETb4k"

Bootstrap(app)
GoogleMaps(app)


@app.route("/")
def hello():
    return render_template('index-simple.html')


@app.route("/map")
def mapview():
    map_data = get_realtor_data()
    map_markers = set_markers(map_data)
    
    mymap = Map(
        identifier="mymap",
        lat=49.0305287,
        lng=-122.80,
        zoom=12,
        markers=map_markers,
    )
    return render_template('map.html', flask_gmap=mymap)


@app.route('/apidata')
def apidata():
    realtor_data = get_realtor_data()
    return jsonify(realtor_data)


@app.route('/csvdata')
def csvdata():
    csv_data = get_csv_data('data/property-sample.csv')
    return jsonify(csv_data)


@app.route('/scraper')
def scraper():
    html = coastcapital()
    return render_template("scraper.html", data = html)


if __name__ == '__main__':
    app.run(debug=True)
