#!/usr/bin/python
#Tue Feb  7 22:50:20 IST 2017
#Mukesh Sharma

import urllib2
import json
import time
import argparse
from prettytable import PrettyTable
#from config import *


#USGS Dataconfig"
config_data = {

        'url':'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/',
        'severities':['all','1.0','2.5','4.5','significant'],
        'timeframe' :['hour','day','week','month'],
        'suffix'    :'.geojson'

        }

#arugment parsing
parser = argparse.ArgumentParser(
        description="Earhquake Data",
        epilog= "severities [ all, 1.0,2.5,4.5,signigicant]\
                time [hour, day,week,month]"
        )
parser.add_argument('sev', help="Enter the severity")
parser.add_argument('time', help='Enter the time')

args = parser.parse_args()

#URL Building
geourl = "{0}{1}_{2}{3}".format(
        config_data['url'],
        args.sev,
        args.time,config_data['suffix']

        )
print "Downloading the data from the URL: " + geourl

#load the JSON data from the geourl
dataset = json.loads(urllib2.urlopen(geourl).read())
print "*" * 22

print dataset['metadata']['title']
print "*" * 22


#filtering json data
data_place= []
data_mag = []
data_coord = []

for i in dataset['features']:
    data_place.append(i['properties']['place'])
    data_mag.append(i['properties']['mag'])
    data_coord.append(i['geometry']['coordinates'])


#pretty table the data
x = PrettyTable()
x.add_column("Place ",data_place)
x.add_column("Magnitude",data_mag)
x.add_column("Coordinates",data_coord)
print x
