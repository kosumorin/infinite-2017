class Station(object):
    def __init__(self, name: str, EWL_id: float = -1, NSL_id: float = -1, CCL_id: float = -1):
        self.name = name
        self.EWL_id = EWL_id
        self.NSL_id = NSL_id
        self.CCL_id = CCL_id
        self.EWL_station_path : 'StationPath' = None
        self.NSL_station_path : 'StationPath' = None
        self.CCL_station_path : 'StationPath' = None

class StationPath(object):
    def __init__(self, up: 'Station' = None, right: 'Station' = None, left: 'Station' = None, down: 'Station' = None):
        self.up = up
        self.right = right
        self.down = down
        self.left = left
