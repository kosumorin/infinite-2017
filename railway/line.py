import utils.color as color
import railway.station as station
from typing import List
from railway.station import Station

class Line(object):
    def __init__(self, color: int, stations: 'List[Station]'):
        self.color = color
        self.stations = stations

EWL = Line(color=color.GREEN, stations=[
    station.JURONG_EAST,
    station.CLEMENTI,
    station.BUONA_VISTA,
    station.OUTRAM_PARK,
    station.CITY_HALL,
    station.BUGIS,
    station.KALLANG,
    station.PAYA_LEBAR,
    station.BEDOK,
    station.TANAH_MERAH,
    station.PASIR_RIS,
    station.CHANGI
])

NSL = Line(color=color.RED, stations=[
    station.JURONG_EAST,
    station.CHUA_CHU_KANG,
    station.WOODLANDS,
    station.YISHUN,
    station.BISHAN,
    station.TOA_PAYOH,
    station.NEWTON,
    station.ORCHARD,
    station.SOMERSET,
    station.DHOBY_GHAUT,
    station.CITY_HALL,
    station.MARINA_BAY
])

CCL = Line(color=color.YELLOW, stations=[
    station.HABOURFRONT,
    station.HAW_PAR_VILLA,
    station.BUONA_VISTA,
    station.HOLLAND_VILLAGE,
    station.BOTANIC_GARDENS,
    station.BISHAN,
    station.SERANGOON,
    station.PAYA_LEBAR,
    station.STADIUM,
    station.ESPLANADE,
    station.DHOBY_GHAUT
])
