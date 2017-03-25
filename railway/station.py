class Station(object):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.station_flow = {}
