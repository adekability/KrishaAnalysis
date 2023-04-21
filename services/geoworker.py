""" geoworker.py - module to manage GEO positions, addresses and directions """
from dataclasses import dataclass
from geopy.geocoders import Nominatim


@dataclass
class GEOWorker:
    """ class GEOWorker - class to manage maps """

    app_name = "krisha_analysis"

    def search(self, search_phrase) -> dict:
        """ search - method to get place's geo information by search phrase """
        search_result = {}
        geolocator = Nominatim(user_agent=self.app_name)
        location = geolocator.geocode(search_phrase)
        try:
            search_result["address"] = location.address
            search_result["longitude"] = location.longitude
            search_result["latitude"] = location.latitude
            search_result["success"] = True
        except AttributeError:
            search_result["success"] = False
        return search_result
