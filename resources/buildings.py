from flask_restful import Resource
import urllib2, os, json
from bs4 import BeautifulSoup

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../tools/buildings.json')

class Buildings(Resource):
    def get(self):
        with open(filename, 'r') as data_file:
            return json.load(data_file)
