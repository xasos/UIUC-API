from flask_restful import Resource
import urllib2, json
from bs4 import BeautifulSoup

request = urllib2.urlopen('http://illinois.edu/ds/facultyListing')
soup = BeautifulSoup(request, 'html.parser')
retval = []
for x in soup.find_all(class_='ws-ds-college-name'):
    collegename = x.a.string
    x = x.next_sibling
    condition = True
    while(condition):
        departmentname = x.span.a.next_sibling.string
        x = x.next_sibling
        for y in x.find_all('li'):
            ret = {}
            ret['collegename'] = collegename
            ret['departmentname'] = departmentname
            ret['link'] = y.a['href']
            ret['email'] = y.a['href'].split('=')[2]
            ret['netid'] = ret['email'].split('@')[0]
            name = y.a.string
            name = name.split(' ')
            ret['firstname'] = name[1]
            ret['lastname'] = name[0].replace(',', '')
            if (len(name) == 3):
                ret['middlename'] = name[2]
            else:
                ret['middlename'] = None
            if (y.span is None):
                ret['role'] = 'None Specified'
            else:
                ret['role'] = y.span.string
            retval.append(ret)
        x = x.next_sibling
        if (x is not None):
        condition = x is not None and x.name != u'br'
finalreturn = {}
finalreturn['data'] = retval
with open('professors.json', 'w') as outfile:
    json.dump(finalreturn, outfile, sort_keys = True, indent = 4)
