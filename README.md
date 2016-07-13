# UIUC API

[![Join the chat at https://gitter.im/xasos/UIUC-Open-Data][gitter-image]][gitter-url] [![Build Status][travis-image]][travis-url]

Unofficial API for the University of Illinois at Urbana-Champaign. Provides data for various services on campus such as Dining, Weather, Wi-Fi, etc. The API is built with Python, Flask + [Flask RESTful](https://github.com/flask-restful/flask-restful), and Redis. Interest in the project was gauged [here](https://www.reddit.com/r/UIUC/comments/2hhlhn/would_anyone_be_interested_in_a_uiuc_open_data_api/
). This is still very much a WIP, so please feel free to [submit an issue](https://github.com/xasos/UIUC-Open-Data/issues/new) or [contribute](https://github.com/xasos/UIUC-Open-Data/blob/master/CONTRIBUTING.md)!

*Note: This is an unofficial API and is not supported or controlled by the University of Illinois at Urbana-Champaign itself. Any questions, comments, feedback or feature requests should be directed to [xasos](https://github.com/xasos) or via an [issue](https://github.com/xasos/UIUC-Open-Data/issues/new) in this repo.*

**Notice**: This API is currently in progess, so all code may not be up-to-date or working! Initial release coming soon :D

## Usage
**Base URL:** http://uiuc-api.herokuapp.com

**Output:** JSON

## Dining Services

Get information about food options from all dining halls.

#### `GET /dining/:hall/:dateFrom/:dateTo`

*Get detailed menus from specific dining halls from a range of dates*

List of Halls:

| Residence Hall | Dining Hall | Hall Nickname | Hall ID |
| -------------- | ----------- | ------------- | ------- |
| Lincoln Avenue (LAR) | Lincoln/Allen Dining Hall | lar | 5 |
| Lincoln Avenue (LAR) | Field of Greens | fieldofgreens  | 12 |
| Lincoln Avenue (LAR) | Leafy! | leafy | 13 |
| Pennsylvania Avenue (PAR) | PAR Dining Hall | par | 2 |
| Pennsylvania Avenue (PAR) | Penn Station | pennstation | 14 |
| Illinois Street (ISR) | ISR Dining Hall | isr | 3 |
| Illinois Street (ISR) | CHOMPS | chomps | 18 |
| Illinois Street (ISR) | Cocina Mexicana | cocinamexicana |10 |
| Illinois Street (ISR) | Taste of Asia | tasteofasia | 17 |
| Ikenberry | Ikenberry Dining Hall | ikenberrydininghall | 1 |
| Ikenberry | 57 North | 57north | 7 |
| Ikenberry | Better Burger | betterburger | 20 |
| Ikenberry | Caffeinator | caffeinator | 9 |
| Ikenberry | Neo Soul Ingredient | neosoulingredient | 21 |
| Florida Avenue (FAR) | FAR Dining Hall | far | 6 |
| Florida Avenue (FAR) | Cracked Egg Café | crackedeggcafe | 8 |
| Florida Avenue (FAR) | Soul Ingredient | soulingredient | 16 |
| Busey-Evans | Busey-Evans Dining Hall | buseyevans | 4 |
| Busey-Evans | Busey Bean and Green | buseybeanandgreen | 11 |
| Busey-Evans | Oodles | oodles | 19 |

*`Hall` route parameter can use the Hall ID or Hall nickname when querying.*

Example Query:
```
http://uiuc-api.herokuapp.com/dining/par/2015-11-08/2015-11-08
```

Response:
```json
{
   "Menus":{
      "Item":[
         {
            "EventDate":1446962400,
            "DiningMenuID":52456,
            "ServiceUnit":"Arugula's Serving",
            "Course":"Salads",
            "CourseSort":250,
            "FormalName":"Fruit & Nut Chicken Salad",
            "Meal":"Dinner",
            "Traits":"Eggs,Soy,Tree Nuts,",
            "DiningOptionID":2,
            "ScheduleID":9,
            "ItemID":5978
         },
         {
            "EventDate":1446962400,
            "DiningMenuID":50688,
            "ServiceUnit":"Arugula's Serving",
            "Course":"Salads",
            "CourseSort":250,
            "FormalName":"Macaroni Salad",
            "Meal":"Dinner",
            "Traits":"Corn,Eggs,Gluten,Soy,Vegetarian,Wheat,",
            "DiningOptionID":2,
            "ScheduleID":9,
            "ItemID":3208
         },
  ...
  ...
```

#### `GET /dining/:hall`

*Get today's menu for each of the dining halls*

Example query:
```
https://uiuc-api.herokuapp.com/dining/par
```


#### `GET /dining/search/:query`


*Search dining halls for specific foods.*

Example Query:
```
http://uiuc-api.herokuapp.com/dining/search/pasta
```

Response:
```json
{
   "Data":{
      "Table":[
         {
            "name":"ItemList",
            "Row":[
               {
                  "Item_IntID":"16596",
                  "FormalName":"BLT Pasta Salad",
                  "ScheduleIDs":[
                     {
                        "ScheduleID":4,
                        "DiningOptionID":4,
                        "EventDate":1447221600
                     }
                  ]
               },
               {
                  "Item_IntID":"17136",
                  "FormalName":"Campanelle Pasta",
                  "ScheduleIDs":[
                     {
                        "ScheduleID":21,
                        "DiningOptionID":5,
                        "EventDate":1447653600
                     },
                     {
                        "ScheduleID":42,
                        "DiningOptionID":1,
                        "EventDate":1447308000
                     },
                     {
                        "ScheduleID":42,
                        "DiningOptionID":1,
                        "EventDate":1447912800
                     }
                  ]
               },
  ...
  ...
```

#### `GET /dining/information`

*Search information on specific dining halls and calorie content for different food .*

Example Query:
```
http://uiuc-api.herokuapp.com/dining/information
```

Response:
```json
{
  "Data":{
    "Table":[
      {
        "Row":[
          {
            "Address":"301 E. Gregory Drive, Champaign",
            "DiningLocation":"Ikenberry Commons",
            "DiningOptionID":1,
            "DiningOptionName":"Ikenberry Dining Hall",
            "MoreInfo":"<p>Located on the first floor of the Student Dining and Residential Programs Building, the Ike features multiple cuisines and made-to-order dishes in this all-you-care-to-eat dining hall. Use a Classic Meal, Café Credits, Extra Credits, or a credit card.</p>",
            "Serving":"('Don''s Chophouse Serving', 'Gregory Street Diner Serving', 'Hortensia''s Serving', 'Penne Lane Serving', 'Prairie Fire Serving', 'Soytainly Serving', 'Euclid Street Deli Serving')",
            "Type":"Classic Dining Hall"
          },
          {
            "Address":"906 W. College Court, Urbana",
            "DiningLocation":"Pennsylvania Avenue (PAR)",
            "DiningOptionID":2,
            "DiningOptionName":"PAR Dining Hall",
            "MoreInfo":"<p>Located downstairs at the Pennsylvania Avenue Residence Halls, the PAR dining hall features multiple cuisines and made-to-order dishes in this all-you-care-to-eat dining hall. Use a Classic Meal, Café Credits, Extra Credits, or a credit card.</p>",
            "Serving":"('Abbondante Serving', 'Arugula''s Serving', 'Better Burger', 'La Avenida Serving', 'Panini Bar', 'Provolone Serving', 'Sky Garden Serving')",
            "Type":"Classic Dining Hall"
          },
	...
	...
```

#### `POST /dining/balance`

*Get University Dining Hall balances and credits.*

Post Parameters:


Example Query:
```
http://uiuc-api.herokuapp.com/dining/balance
```

Response:
```json

  ...
  ...
```

  (https://web.housing.illinois.edu/MobileDining/WebService/SettingTable.aspx?k=7A828F94-620B-4EE3-A56F-328036CC3C04&t=json&ts=5-10-2012%2014:30:00)
  (https://web.housing.illinois.edu/MobileDining/WebService/MyBalances.asmx/GetBalances?k=7A828F94-620B-4EE3-A56F-328036CC3C04&HT=)
  (https://web.housing.illinois.edu/MobileDining/WebService/MobileDining.asmx/SearchMenus?k=7A828F94-620B-4EE3-A56F-328036CC3C04&SearchPhrase=salsa)


## Weather

Get weather information from the [Department of Atmospheric Sciences](https://www.atmos.illinois.edu/weather/).

#### `GET /weather`

*Get Champaign-Urbana weather information from the Williard Airport weather station.*

Example Query:
```
http://uiuc-api.herokuapp.com/weather
```

Response:
```json
  {
    "weather_station_location": "Willard Airport",
    "last_recorded_time": "1446098674",
    "weather_condition": "Cloudy Skies",
    "temperature": "54",
    "dew_point": "45",
    "relative_humidity": "71%",
    "winds": "NW at 17 mph",
    "visibility": "10 miles",
    "pressure": "1020.0 mb (30.13 in)",
    "sunrise": "7:13AM",
    "sunset": "6:01PM",
    "images": {
        "latest_radar_image": "https://www.atmos.illinois.edu/weather/tree/prods/current/nicerad/nicerad_N.gif",
        "storm_total_precip_image": "https://www.atmos.illinois.edu/weather/tree/prods/current/niceradilxpretx/niceradilxpretx_N.gif",
        "surface_temp_image": "https://www.atmos.illinois.edu/weather/tree/prods/current/sfctmp/sfctmp_N.gif",
        "surface_dew_point_temp_image": "https://www.atmos.illinois.edu/weather/tree/prods/current/sfctdp/sfctdp_N.gif",
        "sea_level_pressure": "https://www.atmos.illinois.edu/weather/tree/prods/current/sfcslp/sfcslp_N.gif",
        "mdw_surface_observations": "https://www.atmos.illinois.edu/weather/tree/prods/current/sfcslp/sfcslp_N.gif",
        "composite_ir_image": "https://www.atmos.illinois.edu/weather/tree/prods/current/satconusenhir/satconusenhir_N.gif",
        "composite_enhanced_ir_image": "https://www.atmos.illinois.edu/weather/tree/prods/current/satnoamir/satnoamir_N.gif"
    }
  }
```

## Wi-Fi

Get Wi-Fi information for various places around campus.

#### `GET /wifi`

Example Query:
```
http://uiuc-api.herokuapp.com/wifi
```

Response:
```json
[
  {
    "building":"100 Trade Center, Ste 403",
    "city":"Champaign",
    "state":"IL",
    "street":"100 Trade Center"
  },
  {
    "building":"1001 W. Nevada",
    "city":"Urbana",
    "state":"IL",
    "street":"1001 W. Nevada St."
  },
  ...
  ...
```

#### `GET /wifi/:latitude/:longitude`

Example Query:
```
http://uiuc-api.herokuapp.com/wifi/nearme/40.1140260/-88.2248070
```

Response:
```json
  {
  }
```

## Laundry

Get information about campus laundry.

#### `GET /laundry`

*Get washing machine/dryer usage information for all residence halls.*

Example Query:
```
http://uiuc-api.herokuapp.com/laundry
```

Response:
```json
{
    "location":{
        "name":"University of Illinois at Urbana",
        "code":"urba7723",
        "networked":"false",
        "company":"Jetz Service Co",
        "rooms":[
            {
                "id":"110959186",
                "name":"1107 West Green",
                "networked":"A",
                "machines":[
                    {
                        "port":"1",
                        "label":"1",
                        "description":"Front-Load Washer",
                        "status":"Available",
                        "startTime":"0000-00-00 00:00:00",
                        "timeRemaining":"0"
                    },
                    {
                        "port":"2",
                        "label":"2",
                        "description":"Front-Load Washer",
                        "status":"Available",
                        "startTime":"0000-00-00 00:00:00",
                        "timeRemaining":"0"
                    },
                    {
                        "port":"3",
                        "label":"3",
                        "description":"Front-Load Washer",
                        "status":"Available",
                        "startTime":"0000-00-00 00:00:00",
                        "timeRemaining":"0"
                    },
	...
	...
```

## University Directory

Search the university directory for students, academic departments, and faculty/staff.

#### `GET /directory/search/:searchType/:query`

Search types:

| Search Type | Search Type ID |
| ----------- | --------------- |
| All | all |
| Faculty/Staff | faculty |
| Student | student |
| NetID | netid |
| Department | department |
| Phone | phone |

*`searchType` route parameter can use the Search Type ID when querying.*

Example Query:
```
http://uiuc-api.herokuapp.com/directory/search/netid/npant3
```

Response:
```json
{
	"success": "true",
	"type": "student",
	"email": "npant3@illinois.edu"
}
```

## The Daily Illini

Get stories, classifieds, events, and more from UIUC's campus newspaper, [The Daily Illini](http://www.dailyillini.com/).

#### `GET /dailyillini/search/:query`

*Search the Daily Illini for articles.*

Example Query:
```
http://uiuc-api.herokuapp.com/dailyillini/search/unofficial
```

Response:
```json
{

},
...
```

#### `GET /stories/:category`

*Get stories from different news sections.*

News Sections:

| News Section | News Section ID |
| ----------- | --------------- |
| Campus (inc. Crime/Administration) |  |
| Crime |  |
| Administration |  |
| Champaign-Urbana |  |
| State |  |
| Men's Sports (All-Inclusive) |  |
| Women's Sports |  |
| Sports (All-Inclusive) |  |
| Illini of the Week |  |
| Wheelchair Basketball |  |

Example Query:
```
http://uiuc-api.herokuapp.com/dailyillini/stories/news
```

Response:
```json
{

},
...
```

#### `POST /stories/submit`

Post Parameters:
| News Section | News Section ID |
| ----------- | --------------- |
| Campus (inc. Crime/Administration) |  |
| Crime |  |
| Administration |  |
| Champaign-Urbana |  |
| State |  |
| |  |



Name *

First

Last
Address

Street Address

Address Line 2

City

State / Province / Region

Postal / Zip Code

Country
Phone Number *

###
-
###
-
####
Email *

Your News *










http://www.dailyillini.com/page/submit-a-news-tip

#### `GET /dailyillini/classifieds/:type`

*Search the Daily Illini for articles.*

Example Query:
```
http://uiuc-api.herokuapp.com/dailyillini/search/unofficial
```

Response:
```json
{

},
...
```

## Free Food

Get a list of free food from various events on campus. Data kindly provided by the team at [UIUC Free Food](http://uiucfreefood.com/)!

#### `GET /freefood`

Example Query:
```
http://uiuc-api.herokuapp.com/freefood
```

Response:
```json
[
    {
        "fields":{
            "abbr":"ISB",
            "address":"910 S. FIFTH, CHAMPAIGN",
            "building":"INTERNATIONAL STUDIES BUILDING",
            "calID":"1354",
            "counter":0,
            "displayTime":"11/27 14:00",
            "event":"First Steps Info Session",
            "eventID":"32892600",
            "food":"info session",
            "googleTime":"20151127T185959Z/20151127T195959Z",
            "latLng":"40.1072392,-88.2318771",
            "link":"http://illinois.edu/calendar/detail/1354?eventId=32892600&amp;calMin=201507&amp;cal=20150715&amp;skinId=12775",
            "location":"101 International Studies Building",
            "time":"2015/11/27 14:00-15:00"
        },
        "model":"uiuc.food",
        "pk":545
    },
    {
        "fields":{
            "abbr":"ISB",
            "address":"910 S. FIFTH, CHAMPAIGN",
            "building":"INTERNATIONAL STUDIES BUILDING",
            "calID":"1354",
            "counter":0,
            "displayTime":"12/11 14:00",
            "event":"First Steps Info Session",
            "eventID":"32892601",
            "food":"info session",
            "googleTime":"20151211T185959Z/20151211T195959Z",
            "latLng":"40.1072392,-88.2318771",
            "link":"http://illinois.edu/calendar/detail/1354?eventId=32892601&amp;calMin=201507&amp;cal=20150715&amp;skinId=12775",
            "location":"101 International Studies Building",
            "time":"2015/12/11 14:00-15:00"
        },
        "model":"uiuc.food",
        "pk":546
    }
    ...
    ...
```

#### `GET /calendar`

*Get the Daily Illini event calendar.*

Example Query:
```
http://uiuc-api.herokuapp.com/dailyillini/calendar
```

Response:
```json
{

},
...
```

## Buildings

Get a list of all buildings and building information on campus.

#### `GET /buildings`

Example Query:
```
http://uiuc-api.herokuapp.com/buildings
```

Response:
```json
{ "building1": "",
  "building2": ""
}
```

## EWS Status

Get the availability of EWS (Engineering Workstations) machines across campus.

#### `GET /ews-status`

Example Query:
```
http://uiuc-api.herokuapp.com/ews-status
```

Response:
```json
{
    "data":[
        {
            "inusecount":0,
            "machinecount":100,
            "strlabname":"DCL L416"
        },
        {
            "inusecount":0,
            "machinecount":7,
            "strlabname":"DCL L426"
        },
        {
            "inusecount":0,
            "machinecount":30,
            "strlabname":"DCL L440"
        },
        {
            "inusecount":0,
            "machinecount":41,
            "strlabname":"DCL L520"
        },
        {
            "inusecount":2,
            "machinecount":46,
            "strlabname":"ECEB 2022"
        },
        {
            "inusecount":6,
            "machinecount":17,
            "strlabname":"ECEB 3022"
        },
	...
	...
```

## Atheletic Schedule

Get the Fighting Illini's athletic schedule across all sports.

Sports:

| Search Type | Search Type ID |
| ----------- | --------------- |
| All | all |
| Baseball | baseball |
| Football | football |
| Men's Basketball | mensbasketball |
| Men's Cross Country | mensxc |
| Men's Golf | mensgolf |
| Men's Gymnastics | mensgymanstics |
| Men's Tennis | menstennis |
| Men's Track & Field | menstrack |
| Soccer | soccer |
| Softball | softball |
| Swimming & Diving | swimming |
| Volleyball | volleyball |
| Women's Basketball | womensbball |
| Women's Cross Country | womensxc |
| Women's Golf | womensgolf |
| Women's Gymnastics | womensgymnastics |
| Women's Tennis | womenstennis |
| Women's Track & Field | womenstrack |
| Wrestling | wrestling |


http://app-uiuc-ncaa.yinzcam.com/V1/Game/List/?teamid=uiuc-football&version=4.6&app_version=1.0.1&mcc=310&width=640&application=NCAA_UIUC&schoolid=UIUC&os=iOS&mnc=260&height=1136&os_version=9.1&ff=mobile&carrier=T-Mobile

http://app-uiuc-ncaa.yinzcam.com/V1/Game/List/?teamid=uiuc-mcross&version=4.6&app_version=1.0.1&mcc=310&width=640&application=NCAA_UIUC&schoolid=UIUC&os=iOS&mnc=260&height=1136&os_version=9.1&ff=mobile&carrier=T-Mobile

wcross
wvball
wsoc
mbball
wbball
wswim
mgym
wgym
wrestling
baseball
softball
mgolf
wgolf
mtrack
wtrack
mten
wten

http://app-uiuc-ncaa.yinzcam.com/V1/Media/ShortList/?version=4.6&mcc=310&app_version=1.0.1&width=640&application=NCAA_UIUC&schoolid=UIUC&os=iOS&mnc=260&height=1136&os_version=9.1&ff=mobile&carrier=T-Mobile


http://app-uiuc-ncaa.yinzcam.com/V1/Game/Calendar/?teamid=uiuc-football&version=4.6&app_version=1.0.1&mcc=310&width=640&application=NCAA_UIUC&schoolid=UIUC&os=iOS&mnc=260&height=1136&os_version=9.1&ff=mobile&carrier=T-Mobile

http://app-uiuc-ncaa.yinzcam.com/V1/Team/Players/?teamid=uiuc-football&version=4.6&app_version=1.0.1&mcc=310&width=640&application=NCAA_UIUC&schoolid=UIUC&os=iOS&mnc=260&height=1136&os_version=9.1&ff=mobile&carrier=T-Mobile

http://app-uiuc-ncaa.yinzcam.com/V1/Team/Coaches/?teamid=uiuc-football&version=4.6&app_version=1.0.1&mcc=310&width=640&application=NCAA_UIUC&schoolid=UIUC&os=iOS&mnc=260&height=1136&os_version=9.1&ff=mobile&carrier=T-Mobile

#### `GET /athleticschedule/:sport`

Example Query:
```
http://uiuc-api.herokuapp.com/athleticschedule/menscrosscountry
```

Response:
```json

```

## Course Information
UIUC's Student Services Development Team offers an [API](http://courses.illinois.edu/cisdocs/) for information on Class Schedule, Course Catalog, and Gened data. However, since the data is not publibly available, you must sign up for access [here](http://courses.illinois.edu/cisdocs/authentication).

## Transportation
The Champaign-Urbana Mass Transit District offers an [API](https://developer.cumtd.com/) for transporation information in the Champaign-Urbana metropolitan area. There are several API wrappers and Open-source applications written with the CUMTD API on [GitHub](https://github.com/search?utf8=%E2%9C%93&q=cumtd) as well as in their [App Garage](http://www.cumtd.com/maps-and-schedules/app-garage).

## Run Locally
```sh
$ pip install -r requirements.txt
$ python app.py
```

## Deploy to Heroku
```sh
$ pip install -r requirements.txt
$ heroku create
$ (git add, git commit)
$ git push heroku master
```

## Client Libraries
 - [UIUC.py]() (Python)
 - [node-uiuc]() (Node.js)
 <!--- []() (Java/Android)-->
 <!--- []() (Swift)-->
 <!--- []() (Objective-C)-->
 <!--- []() (Scala)-->
 <!--- []() (Ruby)-->
 <!--- []() (Clojure)-->
 <!--- []() (Golang)-->

*If you've built a wrapper for this API, feel free to add it to this list by sending a PR!*

## Expo
Some apps built using this API:

| Name | Description | URL |
| ---- | ---- | ---- |
| uiuc-cli | CLI to university services | https://github.com/xasos/uiuc-cli |
| UIUC Laundry | iOS application to track UIUC laundry machines | https://github.com/xasos/UIUC-Laundry |

*If you've built an app using this API, feel free to add it to this list by sending a PR!*

## Contributing
Please refer to the [Contributing Guidelines](https://github.com/xasos/UIUC-Open-Data/blob/master/CONTRIBUTING.md) before submitting any pull requests!

## To-Do List
The To-Do List can be found [here](https://github.com/xasos/UIUC-Open-Data/blob/master/todo.md).

## Statistics
So far, x users have used the API and over y requests have been made!

## Disclaimer
Use of this API is purely for educational purposes only, unless otherwise noted.

## License
[MIT License](LICENSE)


[gitter-url]: https://gitter.im/xasos/UIUC-Open-Data?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
[gitter-image]: https://badges.gitter.im/Join%20Chat.svg
[travis-url]: https://travis-ci.org/xasos/UIUC-API
[travis-image]: https://travis-ci.org/xasos/UIUC-API.svg?branch=master
