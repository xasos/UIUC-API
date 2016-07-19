from flask_restful import Resource
import urllib2
from bs4 import BeautifulSoup

years = {'2016':'http://www.senate.illinois.edu/ep0943.html', '2017':'http://www.senate.illinois.edu/ep0944.html', '2018':'http://www.senate.illinois.edu/ep0945.html'}

class Calendar(Resource):
    def get(self, year):
        if year not in years.keys():
            return {'This year':'is not available.'}
        else :
            request_url=years[year]
            request = urllib2.urlopen(request_url)
            soup = BeautifulSoup(request, 'html.parser')
            retval = {}
            for x in soup.find_all('table'):
                retlist = []
                for y in x.find_all('tr'):
                    if (y.td.p is None):
                        retlist.append((y.td.string, y.td.next_sibling.string))
                    else:
                        retlist.append((y.td.p.string, y.td.next_sibling.string))
                retval[x.previous_sibling.previous_sibling.strong.string] = retlist
            return retval;
