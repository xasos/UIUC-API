from flask_restful import Resource
import urllib2
import json

class Dining(Resource):
    def get(self):
      request_url = "https://web.housing.illinois.edu/MobileDining/WebService/Search.aspx?k=7A828F94-620B-4EE3-A56F-328036CC3C04"
      # Add route parameters
      request_url += "?id=" + hallId + "&from=" + fromDate + "&to=" + toDate + "&t=json"
      response = urllib2.urlopen(request_url)
      return json.load(response)


# For dining/info endpoint: https://web.housing.illinois.edu/MobileDining/WebService/SettingTable.aspx?k=7A828F94-620B-4EE3-A56F-328036CC3C04&t=json&ts=5-10-2012%2014:30:00
# for food: https://web.housing.illinois.edu/MobileDining/WebService/Search.aspx?k=7A828F94-620B-4EE3-A56F-328036CC3C04&id=4&from=2015-11-16&to=2015-11-16&t=json


