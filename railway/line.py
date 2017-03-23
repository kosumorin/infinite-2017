from utils.color import Color
from utils.direction import Direction
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
        MRTStation.CLEMENTI,
        MRTStation.BUONA_VISTA,
        MRTStation.CITY_HALL,
        MRTStation.PAYA_LEBAR,
        MRTStation.CHANGI
    ])

    NSL = Line(name="North South Line", color=Color.RED, stations=[
        MRTStation.JURONG_EAST,
        MRTStation.WOODLANDS,
        MRTStation.BISHAN,
        MRTStation.ORCHARD,
        MRTStation.CITY_HALL,
        MRTStation.MARINA_BAY
    ])

    CCL = Line(name="Circle Line", color=Color.YELLOW, stations=[
        MRTStation.HARBOURFRONT,
        MRTStation.HAW_PAR_VILLA,
        MRTStation.BUONA_VISTA,
        MRTStation.BOTANIC_GARDENS,
        MRTStation.BISHAN,
        MRTStation.SERANGOON,
        MRTStation.PAYA_LEBAR,
        MRTStation.ESPLANADE,
        MRTStation.MARINA_BAY
    ])

    MRTStation.JURONG_EAST.station_flow[EWL]    = { "next": Direction.SOUTH }
    MRTStation.CLEMENTI.station_flow[EWL]       = { "next": Direction.EAST, "previous": Direction.NORTH }
    MRTStation.BUONA_VISTA.station_flow[EWL]    = { "next": Direction.EAST, "previous": Direction.WEST }
    MRTStation.CITY_HALL.station_flow[EWL]      = { "next": Direction.EAST, "previous": Direction.WEST }
    MRTStation.PAYA_LEBAR.station_flow[EWL]     = { "next": Direction.EAST, "previous": Direction.WEST }
    MRTStation.CHANGI.station_flow[EWL]         = { "previous": Direction.WEST }

    MRTStation.JURONG_EAST.station_flow[NSL]    = { "next": Direction.NORTH }
    MRTStation.WOODLANDS.station_flow[NSL]      = { "next": Direction.NORTH, "previous": Direction.SOUTH }
    MRTStation.BISHAN.station_flow[NSL]         = { "next": Direction.SOUTH, "previous": Direction.NORTH }
    MRTStation.ORCHARD.station_flow[NSL]        = { "next": Direction.SOUTH, "previous": Direction.NORTH }
    MRTStation.CITY_HALL.station_flow[NSL]      = { "next": Direction.SOUTH, "previous": Direction.NORTH }
    MRTStation.MARINA_BAY.station_flow[NSL]     = { "previous": Direction.NORTH }

    MRTStation.HARBOURFRONT.station_flow[CCL]        = {"next": Direction.EAST}
    MRTStation.HAW_PAR_VILLA.station_flow[CCL]      = { "next": Direction.NORTH, "previous": Direction.WEST }
    MRTStation.BUONA_VISTA.station_flow[CCL]        = { "next": Direction.NORTH, "previous": Direction.SOUTH }
    MRTStation.BOTANIC_GARDENS.station_flow[CCL]    = { "next": Direction.EAST, "previous": Direction.SOUTH }
    MRTStation.BISHAN.station_flow[CCL]             = { "next": Direction.EAST, "previous": Direction.WEST }
    MRTStation.SERANGOON.station_flow[CCL]          = { "next": Direction.SOUTH, "previous": Direction.WEST }
    MRTStation.PAYA_LEBAR.station_flow[CCL]         = { "next": Direction.SOUTH, "previous": Direction.NORTH }
    MRTStation.ESPLANADE.station_flow[CCL]          = { "next": Direction.WEST, "previous": Direction.NORTH }
    MRTStation.MARINA_BAY.station_flow[CCL]         = { "previous": Direction.EAST }

