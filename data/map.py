from railway.line import Line
from railway.station import Station
from utils.direction import Direction
from utils.color import Color

import os
import json

# Loads JSON file based on main.py's absolute path!
map_file = open(os.path.abspath("./data/map.json"), "r")
map_data = json.loads(map_file.read())
map_file.close()

# Helper method for MRTStations
def convert_station_flow(station_flow: 'Dict[]'):
    new_station_flow = {}

    for key in station_flow.keys():
        new_station_flow[key] = {}

        for inner_key in station_flow[key].keys():
            direction = station_flow[key][inner_key]

            if direction == "NORTH":
                new_station_flow[key][inner_key] = Direction.NORTH
            elif direction == "EAST":
                new_station_flow[key][inner_key] = Direction.EAST
            elif direction == "SOUTH":
                new_station_flow[key][inner_key] = Direction.SOUTH
            elif direction == "WEST":
                new_station_flow[key][inner_key] = Direction.WEST

    return new_station_flow

def convert_to_color(color: str) -> 'Color':
    if color.upper() == "INVALID":
        return Color.INVALID
    elif color.upper() == "BLACK":
        return Color.BLACK
    elif color.upper() == "BLUE":
        return Color.BLUE
    elif color.upper() == "GREEN":
        return Color.GREEN
    elif color.upper() == "YELLOW":
        return Color.YELLOW
    elif color.upper() == "RED":
        return Color.RED
    elif color.upper() == "WHITE":
        return Color.WHITE
    elif color.upper() == "BROWN":
        return Color.BROWN

class MRTStations(object):
    stations_data = map_data["stations"]
    stations = []

    for station in stations_data:
        s = Station(station["id"], station["name"])
        s.station_flow = convert_station_flow(station["station_flow"])

        stations.append(s)

    @classmethod
    def get_station_by_name(cls, name: str) -> 'Station':
        for station in cls.stations:
            if station.name.lower() == name.lower():
                return station

    @classmethod
    def get_station_by_id(cls, id: int) -> 'Station':
        for station in cls.stations:
            if station.id == id:
                return station

# Helper method for MRTLines
def get_stations_by_ids(station_ids: 'List[int]') -> 'List[Station]':
    stations = []

    for id in station_ids:
        stations.append(MRTStations.get_station_by_id(id))

    return stations

class MRTLines(object):
    lines_data = map_data["lines"]
    lines = []

    for line in lines_data:
        l = Line(line["name"], convert_to_color(line["color"]), get_stations_by_ids(line["station_ids"]))

        lines.append(l)

    @classmethod
    def get_line_by_name(cls, name: str) -> 'Line':
        for line in cls.lines:
            if line.name.lower() == name.lower():
                return line
