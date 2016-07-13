import urllib2, json
from bs4 import BeautifulSoup

request = urllib2.urlopen('http://fs.illinois.edu/about-us/building-list-by-building-number')
soup = BeautifulSoup(request, 'html.parser')
retval = []
for x in soup.find_all('tr'):
    ret = {}
    ret['number'] = x.contents[1].string
    ret['name'] = x.contents[3].string
    if (x.contents[5] is None):
        ret['address'] = None
    else:
        ret['address'] = x.contents[5].string
    if (x.contents[7] is None):
        ret['city'] = None
    else:
        ret['city'] = x.contents[7].string
    if (len(x.contents) < 10 or x.contents[9] is None):
        ret['zipcode'] = None
    else:
        ret['zipcode'] = x.contents[9].string
    retval.append(ret)
finalreturn = {}
finalreturn['data'] = retval
with open('buildings.json', 'w') as outfile:
    json.dump(finalreturn, outfile, sort_keys = True, indent = 4)
