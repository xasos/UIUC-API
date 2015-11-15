from flask_restful import Resource
from bs4 import BeautifulSoup
import urllib2
import geocoder
import json

class Wifi(Resource):
    def get(self):
        request_url = "https://www.cites.illinois.edu/wireless/locations.html"
        response = urllib2.urlopen(request_url)
        soup = BeautifulSoup(response, "html.parser")
        soup.find_all('font')
        geocode = geocoder.google(address)
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        return json.load(response)

