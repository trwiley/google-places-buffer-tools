# scrapebuffer.py
# purpose: to use the Google Places API in order to scrape locations from a given radius


import googlemaps
import time
import json

from places import PLACES

class Scraper:
    def __init__(self, lat, longi, radius, API_KEY, filename):
        self._lat = lat
        self._long = longi
        self._radius = radius
        self._API_KEY = API_KEY
        self._mapsvc = googlemaps.Client(API_KEY)
        self._results = []
        self._filename = filename

    def get_from_google(self):
        for p in PLACES:
            print('adding places of type', p)
            self.get_types_nearby(p)
        
    def get_types_nearby(self, atype):
        # grab all places of a certain type within a given radius of a centerpoint.
        query = self._mapsvc.places_nearby(location=(self._lat, self._long), radius=self._radius, type=atype)
        self._results += query['results']
        if 'next_page_token' in query.keys():
                nextpagetoken = query['next_page_token']
                time.sleep(2)
        else:
                nextpagetoken = ''

        while nextpagetoken != '':
            query = self._mapsvc.places_nearby(location=(self._lat, self._long), radius=self._radius, page_token=nextpagetoken)
            self._results += query['results']
            if 'next_page_token' in query.keys():
                nextpagetoken = query['next_page_token']
                time.sleep(2)
            else:
                nextpagetoken = ''
        


    def write_to_json(self):
        with open(self._filename, 'w') as fp:
            json.dump(self._results, fp)
    
    def __add__(self, val):
        new_scrape = Scraper(self._lat, self._long, self._radius, self._API_KEY, self._filename)
        new_scrape._results =  self._results + val._results
        return new_scrape




