from utils.color import Color
from railway.station import Station

class Line(object):
    def __init__(self, name: str, color: 'Color', stations: 'List[Station]'):
        self.name = name
        self.color = color
        self.stations = stations

    def get_station_index(self, target_station: 'Station') -> int:
        for i in range(0, len(self.stations)):
            if self.stations[i] == target_station:
                return i

        return -1

    def get_intersecting_stations(self, target_line: 'Line') -> 'List[Station]':
        intersecting_stations = []

        for station_curr in self.stations:
            for station_tgt in target_line.stations:
                if station_curr == station_tgt:
                    intersecting_stations.append(station_curr)

        return intersecting_stations
