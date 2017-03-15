from typing import Dict
from utils.direction import Direction

class Station(object):
    def __init__(self, name: str):
        self.name = name
        self.line_flow: 'Dict[Line, Direction]' = {}

class MRTStation(object):
    CHANGI = Station("Changi")
    PAYA_LEBAR = Station("Paya Lebar")
    CITY_HALL = Station("City Hall")
    BUONA_VISTA = Station("Buona Vista")
    JURONG_EAST = Station("Jurong East")
    MARINA_BAY = Station("Marina Bay")
    BISHAN = Station("Bishan")
    WOODLANDS = Station("Woodlands")
    ESPLANADE = Station("Esplanade")
    HAW_PAR_VILLA = Station("Haw Par Villa")
    HABOURFRONT = Station("Habourfront")
