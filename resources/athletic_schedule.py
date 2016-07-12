from flask_restful import Resource
import urllib2
from bs4 import BeautifulSoup
import xml2json


BASE_URL = "http://www.fightingillini.com/schedule.aspx?path="

sports = ['baseball', 'mbball', 'mcross', 'football', 'mgolf',
            'mgym', 'mten', 'mtrack', 'wrestling', 'wbball',
            'wcross', 'wgolf', 'wgym', 'wsoc', 'softball',
            'wswim', 'wten', 'wtrack', 'wvball']

'''class AthleticSchedule(Resource):
    def get(self, sport):
        request_url = 'http://app-uiuc-ncaa.yinzcam.com/V1/Game/List/?teamid=uiuc-' + sport + '&version=4.6&app_version=1.0.1&mcc=310&width=640&application=NCAA_UIUC&schoolid=UIUC&os=iOS&mnc=260&height=1136&os_version=9.1&ff=mobile&carrier=T-Mobile'
        request = urllib2.urlopen(request_url)
        print(type(request))
        return xml2json.xml2json(request.read(), None)'''

class AthleticSchedule(Resource):
    def get(self, sport):
        if sport.lower() in sports:
            request_url = BASE_URL + sport
            req = urllib2.Request(request_url, None, {'User-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
            request = urllib2.urlopen(req)
            soup = BeautifulSoup(request, 'html.parser')
            retval = {}
            gamelist = []
            for x in soup.find_all(class_='schedule_game'):
                print(x)
                game = {}
                if (x.find(class_='schedule_game_opponent_name').a is None and x.find(class_='schedule_game_opponent_name').span is None):
                    game['Opponent'] = x.find(class_='schedule_game_opponent_name').string.strip()
                elif (x.find(class_='schedule_game_opponent_name').span is None):
                    if (x.find(class_='schedule_game_opponent_name').a.string is None):
                        game['Opponent'] = x.find(class_='schedule_game_opponent_name').a.span.string.strip()
                    else:
                        game['Opponent'] = x.find(class_='schedule_game_opponent_name').a.string.strip()
                else:
                    game['Opponent'] = x.find(class_='schedule_game_opponent_name').span.string.strip()
                game['Date'] = x.find(class_='schedule_game_opponent_date').string.strip()
                game['Time'] = x.find(class_='schedule_game_opponent_time').string.strip()
                if (x.find(class_='schedule_game_location').span is None):
                    game['Location'] = x.find(class_='schedule_game_location').string.strip()
                else:
                    if (x.find(class_='schedule_game_location').span.string is None):
                        game['Location'] = None
                    else:
                        game['Location'] = x.find(class_='schedule_game_location').span.string.strip()
                #game['Home/Away'] = x.find(class_='schedule_game_location').span['class'][0].split('_')[1]
                #game['Watchable Links'] = x.find(class_='schedule_game_links').span['class'].split('_')[1]
                if (x.find(class_='schedule_game_results') is None or len(x.find(class_='schedule_game_results').div.contents) == 0):
                    game['Results'] = 'This has not happened yet or no results were reported'
                else:
                    game['Results'] = (x.find(class_='schedule_game_results').div.contents[0])
                gamelist.append(game)
            retval['games'] = gamelist
            return retval
        else:
            return {'This sport' : 'does not exist'}
