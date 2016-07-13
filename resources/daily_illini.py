from flask_restful import Resource
import urllib2, json
from bs4 import BeautifulSoup

base_url = 'http://dailyillini.com/category/'

def scraper(url):
    retval = {}
    for i in range(1, 6):
        try:
            request = urllib2.urlopen(urllib2.Request(url + 'page/' + str(i), None, {'User-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}))
        except urllib2.HTTPError:
            break
        soup = BeautifulSoup(request, 'html.parser')
        retlist = []
        for j in range(len(soup.find_all(class_='sno-animate')) - 4):
            x = soup.find_all(class_='sno-animate')[j]
            ret = {}
            ret['title'] = x.h1.a.string
            ret['link'] = x.h1.a['href']
            if (x.p.contents[1].name != u'a'):
                ret['date'] = x.p.contents[0]
                ret['journalist'] = None
            else :
                ret['journalist'] = x.p.contents[1].string
                if (x.p.contents[2].name is None):
                    ret['date'] = x.p.contents[4]
                else:
                    ret['date'] = x.p.contents[3]
            if (len(x.p.next_sibling.contents) == 0):
                ret['partialtext'] = None
            else:
                ret['partialtext'] = x.p.next_sibling.contents[0].string
            retlist.append(ret)
        retval['Page ' + str(i)] = retlist
    return retval


class News(Resource):
    def get(self, category):
        request_url = base_url + category + '/'
        return scraper(request_url)

class SubCategoryNews(Resource):
    def get(self, category, subcategory):
        request_url = base_url + category + '/' + subcategory + '/'
        return scraper(request_url)

class SportsNews(Resource):
    def get(self, category, subcategory, sportcategory):
        request_url = base_url + category + '/' + subcategory + '/' + sportcategory + '/'
        return scraper(request_url)

class RecentNews(Resource):
    def get(self):
        request_url = 'http://dailyillini.com/feed/'
        request = urllib2.urlopen(urllib2.Request(request_url, None, {'User-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}))
        soup = BeautifulSoup(request, 'lxml')
        retval = []
        for x in soup.find_all('item'):
            ret = {}
            ret['title'] = x.title.string
            ret['link'] = x.a['href']
            ret['date'] = x.contents[7].string
            retval.append(ret)
        return {'data':retval}


if __name__ == '__main__':
    scraper('http://dailyillini.com/category/news/champaign-urbana/')
