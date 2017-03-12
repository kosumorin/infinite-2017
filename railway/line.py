from utils.color import *
from railway.station import *
from typing import List

class Line(object):
    def __init__(self, color: int, stations: 'List[Station]'):
        self.color = color
        self.stations = stations

EWL_Line = Line(color=GREEN, stations=EWL_STATIONS)
NSL_Line = Line(color=RED, stations=NSL_STATIONS)
CCL_Line = Line(color=YELLOW, stations=CCL_STATIONS)
