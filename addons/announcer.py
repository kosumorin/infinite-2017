from ev3dev.ev3 import Sound
from vehicle.driver import DriverListener

class Announcer(DriverListener):
    def on_station_reached(self, station: 'Station', line: 'Line'):
        Sound.beep().wait()

    def on_end_station_reached(self, station: 'Station', line: 'Line'):
        Sound.play("./assets/jingle.wav").wait()
        Sound.speak(station.name).wait()
