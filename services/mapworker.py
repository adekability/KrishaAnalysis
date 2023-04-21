""" mapworker.py - module to manage MapWorker """
from dataclasses import dataclass
import folium


@dataclass
class MapWorker:
    """ class MapWorker - class to manage map coordinates and render to html page """

    latitude: float
    longitude: float

    def fetch_map_by_coordinates(self):
        """ fetch_map_by_coordinates - method to fetch map by latitude and longitude attributes """
        folium_map = folium.Map(
            location=[self.longitude, self.latitude],
            zoom_start=23,
            width="50%",
            height="50%"
        )
        marker_coordinates = [[self.longitude, self.latitude]]

        for location in marker_coordinates:
            folium.Marker(location=location).add_to(folium_map)
        return folium_map._repr_html_()
