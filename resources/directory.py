from flask_restful import Resource
import urllib2
from bs4 import Beautifulsoup
import re

class StaffDirectory(Resource):
    def get(self, query, search_type):  # construct URL
      request_url = "https://illinois.edu/ds/search?skinId=0&sub=&search=niraj+pant&search_type=staff";
      response = urllib2.urlopen(request_url)
