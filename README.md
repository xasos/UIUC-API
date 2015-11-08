# UIUC Open Data API

[![Join the chat at https://gitter.im/xasos/UIUC-Open-Data](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/xasos/UIUC-Open-Data?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

<!--[![Build Status][travis-image]][travis-url] [![Requirements Status][require-image]][require-url]-->

Unofficial Open Data API for the University of Illinois at Urbana-Champaign. Provides data for various services on campus such as Dining, Weather, Wi-Fi, etc. The API is built with Python, Flask + [Flask RESTful](https://github.com/flask-restful/flask-restful), and Redis. Interest in the project was gauged [here](https://www.reddit.com/r/UIUC/comments/2hhlhn/would_anyone_be_interested_in_a_uiuc_open_data_api/
). This is still very much a WIP, so please feel free to [submit an issue](https://github.com/xasos/UIUC-Open-Data/issues/new) or [contribute](https://github.com/xasos/UIUC-Open-Data/blob/master/CONTRIBUTING.md)!

*Note: This is an unofficial API and is not supported or controlled by the University of Illinois at Urbana-Champaign itself. Any questions, comments, feedback or feature requests should be directed to xasos or via an issue in this repo.*

## Usage
**Base URL:** http://uiuc-api.herokuapp.com

**Output:** JSON

## Dining Services

Get information about food options from all dining halls.

#### `GET /dining/:hall/:dateFrom/:dateTo`

*Get detailed menus from specific dining halls.*

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

#### `GET /dining/`

Example Query:
```
http://uiuc-api.herokuapp.com/dining/search/pasta
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
    },
    "": ""
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
  {
    "weather_station_location": "Willard Airport"
  }
```

#### `GET /wifi/nearme/:latitude/:longitude` 
<!-- Switch to query-based parameters and add section -->

Example Query:
```
http://uiuc-api.herokuapp.com/wifi
```

Response:
```json
  {
    "weather_station_location": "Willard Airport"
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
	"location": {
		"name": "University of Illinois at Urbana",
		"code": "urba7723",
		"networked": "false",
		"company": "Jetz Service Co",
		"rooms": [{
			"id": "110959186",
			"name": "1107 West Green",
			"networked": "A",
			"machines": [{
				"port": "1",
				"label": "1",
				"description": "Front-Load Washer",
				"status": "Available",
				"startTime": "0000-00-00 00:00:00",
				"timeRemaining": "0"
			}, {
				"port": "2",
				"label": "2",
				"description": "Front-Load Washer",
				"status": "Available",
				"startTime": "0000-00-00 00:00:00",
				"timeRemaining": "0"
			}, {
				"port": "3",
				"label": "3",
				"description": "Front-Load Washer",
				"status": "Available",
				"startTime": "0000-00-00 00:00:00",
				"timeRemaining": "0"
			},
			...
			...
```




### Course Information

### University Directory
 - /directory/search/:searchType/:query
 - 
 
## Faculty/Department

## The Daily Illini

## Transportation
The Champaign-Urbana Mass Transit District offers an [API](https://developer.cumtd.com/) for transporation information in the Champaign-Urbana metropolitan area. There are several API wrappers and Open-source applications written with the CUMTD API on [GitHub](https://github.com/search?utf8=%E2%9C%93&q=cumtd) as well as in their [App Garage](http://www.cumtd.com/maps-and-schedules/app-garage).
 
## Run Locally
```sh
$ pip install -r requirements.txt
$ python api.py
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
 - []() (Java/Android)
 - []() (Swift)
 - []() (Objective-C)
 - []() (Scala)
 - []() (Ruby)
 - []() (Clojure)
 - []() (Golang)
 
*If you've built a wrapper for this API, feel free to add it to this list by sending a PR!*
 
## Expo
Some apps built using this API: 

| Name | Description | URL |
| ---- | ---- | ---- |
| uiuc-cli | CLI to university services | https://github.com/xasos/uiuc-cli |

*If you've built an app using this API, feel free to add it to this list by sending a PR!*
 
## Statistics
So far, x users have used the API and over y requests have been made!

## Disclaimer
Use of this API

## Todo
- contributing.md
- front-end
- cli
- client libraries
- transportation
- generate google calendar
- uiuc calendar
- department events/seminars
- wiki
- buildings
- Networking, Lens API 
- https://techservices.illinois.edu/services/campus-lightweight-directory-access-protocol
- to do list
- document (hehehehe) code
- clean up code (a lot)
- seperate code into files and add into directory
- add static counter (as text file/button?)
- overarching py file that runs models
- seperate documentation md files for each endpoint
- request for features
- table of values for requests (like meerkat api)
- contributing guidelines
- format dining options data
- route parameter description
- food calories

## Contributing
Please refer to the [Contributing Guidelines](https://github.com/xasos/UIUC-Open-Data/blob/master/CONTRIBUTING.md) before submitting any pull requests.

## License
[MIT License](LICENSE)

throw in some redis/memcache for less server usage

[travis-url]: https://travis-ci.org/xasos/UIUC-Open-Data
[travis-image]: https://travis-ci.org/xasos/UIUC-Open-Data.svg?branch=master
[require-image]: https://requires.io/github/xasos/UIUC-Open-Data/requirements.svg?branch=master
[require-url]: https://requires.io/github/xasos/UIUC-Open-Data/requirements/?branch=master
[daviddm-url]: https://david-dm.org/xasos/Coins.svg?theme=shields.io
[daviddm-image]: https://david-dm.org/xasos/Coins
