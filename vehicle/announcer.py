from ev3dev import ev3
from vehicle.driver import DriverListener


class Announcer(DriverListener):
    def on_station_reached(self, station: 'Station', line: 'Line'):
        ev3.Sound.beep()
