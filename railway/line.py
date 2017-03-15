from utils.color import Color
from utils.direction import Direction
from typing import List
from railway.station import Station, MRTStation

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

class MRTLine(object):
    EWL = Line(name="East West Line", color=Color.GREEN, stations=[
        MRTStation.JURONG_EAST,
        MRTStation.BUONA_VISTA,
        MRTStation.CITY_HALL,
        MRTStation.PAYA_LEBAR,
        MRTStation.CHANGI
    ])

    NSL = Line(name="North South Line", color=Color.RED, stations=[
        MRTStation.JURONG_EAST,
        MRTStation.WOODLANDS,
        MRTStation.BISHAN,
        MRTStation.CITY_HALL,
        MRTStation.MARINA_BAY
    ])

    CCL = Line(name="Circle Line", color=Color.YELLOW, stations=[
        MRTStation.HABOURFRONT,
        MRTStation.HAW_PAR_VILLA,
        MRTStation.BUONA_VISTA,
        MRTStation.BISHAN,
        MRTStation.PAYA_LEBAR,
        MRTStation.ESPLANADE,
        MRTStation.MARINA_BAY
    ])

    MRTStation.JURONG_EAST.line_flow[EWL] = Direction.EAST
    MRTStation.JURONG_EAST.line_flow[NSL] = Direction.NORTH
    MRTStation.BUONA_VISTA.line_flow[EWL] = Direction.EAST
    MRTStation.BUONA_VISTA.line_flow[CCL] = Direction.NORTH
    MRTStation.CITY_HALL.line_flow[EWL] = Direction.EAST
    MRTStation.CITY_HALL.line_flow[NSL] = Direction.SOUTH
    MRTStation.BISHAN.line_flow[CCL] = Direction.EAST
    MRTStation.BISHAN.line_flow[NSL] = Direction.SOUTH
    MRTStation.PAYA_LEBAR.line_flow[EWL] = Direction.EAST
    MRTStation.PAYA_LEBAR.line_flow[CCL] = Direction.SOUTH
    MRTStation.MARINA_BAY.line_flow[NSL] = Direction.EAST
    MRTStation.MARINA_BAY.line_flow[CCL] = Direction.WEST
