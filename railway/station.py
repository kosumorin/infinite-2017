class Station(object):
    def __init__(self, name: str):
        self.name = name
        self.EWL_station_path: 'StationPath' = None
        self.NSL_station_path: 'StationPath' = None
        self.CCL_station_path: 'StationPath' = None

class StationPath(object):
    def __init__(self, up: 'Station' = None, right: 'Station' = None, left: 'Station' = None, down: 'Station' = None):
        self.up = up
        self.right = right
        self.down = down
        self.left = left
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
