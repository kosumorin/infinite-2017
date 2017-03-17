from railway.station import Station
from railway.line import Line, MRTLine
from train.train import Train, TrainListener
from utils.direction import TurnDirection

class MRTDriver(TrainListener):
    def __init__(self, route: 'Route'):
        self.route = route
        self.current_MRT_line = route.start_line
        self.listeners = []

    def on_black(self, train: 'Train', left: bool, right: bool):
        train.stop()

    def on_blue(self, train: 'Train', left: bool, right: bool):
        train.stop()

    def on_green(self, train: 'Train', left: bool, right: bool):
        if self.route.path != 0:
            if self.current_MRT_line == MRTLine.EWL:
                if left:
                    train.steer_left()
                elif right:
                    train.steer_right()

    def on_yellow(self, train: 'Train', left: bool, right: bool):
        if self.route.path != 0:
            if self.current_MRT_line == MRTLine.CCL:
                if left:
                    train.steer_left()
                elif right:
                    train.steer_right()

    def on_red(self, train: 'Train', left: bool, right: bool):
        if self.route.path != 0:
            if self.current_MRT_line == MRTLine.NSL:
                if left:
                    train.steer_left()
                elif right:
                    train.steer_right()

    def on_white(self, train: 'Train', left: bool, right: bool):
        if self.route.path != 0:
            if left and right:
                train.move_forward()

    def on_brown(self, train: 'Train', left: bool, right: bool):
        train.stop()

    def on_click(self, train: 'Train'):
        if self.route.path == 0:
            return
        else:
            station = self.route.path.pop(0)

        for listener in self.listeners:
            listener.on_station_reached(station, self.current_MRT_line)

        if station == self.route.end_station:
            train.stop()

            for listener in self.listeners:
                listener.on_end_station_reached(station, self.current_MRT_line)

            return

        if station == self.route.transfer_station:
            if self.route.transfer_turn_direction == TurnDirection.LEFT:
                train.turn_left()
            elif self.route.transfer_turn_direction == TurnDirection.RIGHT:
                train.turn_right()

            self.current_MRT_line = self.route.end_line

        train.move_forward()

    def add_listener(self, listener: 'MRTDriverListener'):
        self.listeners.append(listener)

class MRTDriverListener(object):
    def on_station_reached(self, station: 'Station', line: 'Line'):
        pass

    def on_line_change(self, station: 'Station', curr_line: 'Line', target_line: 'Line'):
        pass

    def on_end_station_reached(self, station: 'Station', line: 'Line'):
        pass