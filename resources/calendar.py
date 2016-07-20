from flask_restful import Resource
import urllib2
from bs4 import BeautifulSoup


base_url = 'http://www.senate.illinois.edu/'
years = {}
request = urllib2.urlopen('http://www.senate.illinois.edu/a_calendar.asp')
soup = BeautifulSoup(request, 'html.parser')
for x in soup.find('table').find_all('a'):
    if x['href'].split('.')[1] == 'html':
        years[x.string.split('-')[0]] = base_url + x['href']

class Calendar(Resource):
    def get(self, year):
        if year not in years.keys():
            return {'This year':'is not available.'}
        else :
            request_url=years[year]
            request = urllib2.urlopen(request_url)
            soup = BeautifulSoup(request, 'html.parser')
            retval = {}
            i = 1
            for x in soup.find_all('table'):
                retdict = {}
                for y in x.find_all('tr'):
                    if (y.td.p is None):
                        retdict[y.td.string.strip()] = y.td.next_sibling.next_sibling.string.strip()
                    elif (y.td.p.string is None):
                        retdict[y.td.p.contents[0]] = y.td.next_sibling.next_sibling.string.strip()
                    else:
                        retdict[y.td.p.string.strip()] =  y.td.next_sibling.next_sibling.string.strip()
                if (x.previous_sibling.previous_sibling.strong is None):
                    if (x.previous_sibling.previous_sibling.string is None):
                        retval[x.previous_sibling.previous_sibling.contents[0]] = retdict
                    else:
                        retval[x.previous_sibling.previous_sibling.string] = retdict
                else:
                    retval[x.previous_sibling.previous_sibling.strong.string] = retdict
                i+=1;
                if (i == len(soup.find_all('table'))):
                    break
            return retval;
