from utils.color import Color
from typing import List
from railway.station import Station

class Line(object):
    def __init__(self, color: 'Color', stations: 'List[Station]'):
        self.color = color
        self.stations = stations