from railway.station import Station
from railway.line import Line
from data.map import MRTLines, MRTStations
from utils.direction import MovementDirection

import json

def convert_movement_flow(movement_flow: 'list') -> 'list':
    converted_movement_flow = []

    for movement in movement_flow:
        if movement == "STRAIGHT":
            converted_movement_flow.append(MovementDirection.STRAIGHT)
        elif movement == "LEFT":
            converted_movement_flow.append(MovementDirection.LEFT)
        elif movement == "RIGHT":
            converted_movement_flow.append(MovementDirection.RIGHT)

    return converted_movement_flow;

def convert_station_path(station_path: 'list') -> 'list':
    converted_station_path = []

    for station in station_path:
        converted_station_path.append(MRTStations.get_station_by_name(station["name"]))

    return converted_station_path

class Route(object):
    def __init__(self, start_station: 'Station', end_station: 'Station', start_line: 'Line', end_line: 'Line', transfer_station: 'Station', station_path: 'list', movement_flow: 'list'):
        self.start_station = start_station
        self.end_station = end_station
        self.start_line = start_line
        self.end_line = end_line
        self.transfer_station = transfer_station
        self.station_path = station_path
        self.movement_flow = movement_flow

    @staticmethod
    def convert_from_JSON(JSON) -> 'Route':
        converted_JSON = json.loads(JSON)

        start_station = MRTStations.get_station_by_id(converted_JSON["start_station"]["id"])
        end_station = MRTStations.get_station_by_id(converted_JSON["end_station"]["id"])
        start_line = MRTLines.get_line_by_name(converted_JSON["start_line"]["name"])
        end_line = MRTLines.get_line_by_name(converted_JSON["end_line"]["name"])
        station_path = convert_station_path(converted_JSON["station_path"])
        movement_flow = convert_movement_flow(converted_JSON["movement_flow"])

        if len(converted_JSON["transfer_station"]) is None:
            transfer_station = None
        else:
            transfer_station = MRTStations.get_station_by_id(converted_JSON["transfer_station"]["id"])

        return Route(start_station, end_station, start_line, end_line, transfer_station, station_path, movement_flow)