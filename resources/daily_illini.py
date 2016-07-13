from flask_restful import Resource
import urllib2, json,
from bs4 import BeautifulSoup

base_url = 'http://dailyillini.com/category/'

class News(Resource):
    def get(self, category, subcategory=None, sportcategory=None):
        request_url = base_url + category
        if (subcategory is not None):
            request_url += '/' + subcategory
            if (sportcategory is not None):
                request_url += '/' + sportcategory
        fail = False
        i = 1
        retval = {}
        while(!fail):
            request = urllib2.urlopen(request_url)
            soup = BeautifulSoup(request, 'html.parser')
            retlist = []
            for x in soup.find_all(class_='sno-animate'):
                print(x)
            fail = True;
