from railway.station import Station
from railway.line import Line
from train.train import Train, TrainListener

class DriverListener(object):
    def on_station_reached(self, station: 'Station', line: 'Line'):
        pass

    def on_line_change(self, station: 'Station', curr_line: 'Line', target_line: 'Line'):
        pass

    def on_end_station_reached(self, station: 'Station', line: 'Line'):
        pass

class BaseDriver(TrainListener):
    def on_black(self, train: 'Train', left: bool, right: bool):
        train.stop()

    def on_blue(self, train: 'Train', left: bool, right: bool):
        train.stop()

    def on_green(self, train: 'Train', left: bool, right: bool):
        train.stop()

    def on_yellow(self, train: 'Train', left: bool, right: bool):
        train.stop()

    def on_red(self, train: 'Train', left: bool, right: bool):
        train.stop()

    def on_white(self, train: 'Train', left: bool, right: bool):
        if left and right:
            train.move_forward()

    def on_brown(self, train: 'Train', left: bool, right: bool):
        train.stop()

class EWLDriver(BaseDriver):
    def on_green(self, train: 'Train', left: bool, right: bool):
        if left:
            train.turn_left()
        elif right:
            train.turn_right()

class NSLDriver(BaseDriver):
    def on_red(self, train: 'Train', left: bool, right: bool):
        if left:
            train.turn_left()
        if right:
            train.turn_right()

class CCLDriver(BaseDriver):
    def on_yellow(self, train: 'Train', left: bool, right: bool):
        if left:
            train.turn_left()
        elif right:
            train.turn_right()