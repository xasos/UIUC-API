from flask_restful import Resource
from bs4 import BeautifulSoup
import urllib2
import geocoder
import json
import re

class Wifi(Resource):
    def get(self):
        request_url = "http://web.archive.org/web/20151229092233/https://www.cites.illinois.edu/wireless/locations.html"
        response = urllib2.urlopen(request_url)
        soup = BeautifulSoup(response, "html.parser")
        addresses = []
        for x in range(0, 313):
            data = {}
            data["building"] = str(soup.find_all('span')[(6 * x)])
            match = re.compile(r'<a href=.*?>(.*?)<\/a>')
            data["building"] = match.search(data["building"]).group(1)
            data["street"] = str(soup.find_all('span')[(6 * x) + 3])
            match = re.compile(r'>(.*?)<\/span>')
            data["street"] = match.search(data["street"]).group(1)
            data["city"] = str(soup.find_all('span')[(6 * x) + 5])
            match = re.compile(r'>(.*?)<\/span>')
            data["city"] = match.search(data["city"]).group(1)
            data["state"] = "IL"

            #geocode = geocoder.google(data["street"] + " " + data["city"] + " " + data["state"])
            #data["latitude"] = geocode.latlng[0]
            #data["latitude"] = geocode.latlng[1]
            addresses.append(data)

        return addresses

class WifiNearMe(Resource):
  def get(self):
      return ""
