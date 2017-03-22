from railway.station import Station
from railway.line import Line, MRTLine
from train.robot import Robot, RobotListener
from utils.direction import TurnDirection

class Driver(RobotListener):
    def __init__(self, route: 'Route'):
        self.route = route
        self.current_MRT_line = route.start_line
        self.listeners = []

    def on_invalid(self, train: 'Robot', left: bool, right: bool):
        if len(self.route.path) != 0:
            train.move_forward()
        else:
            train.stop()

    def on_black(self, train: 'Robot', left: bool, right: bool):
        if len(self.route.path) != 0:
            train.move_forward()
        else:
            train.stop()

    def on_blue(self, train: 'Robot', left: bool, right: bool):
        if len(self.route.path) != 0:
            train.move_forward()
        else:
            train.stop()

    def on_green(self, train: 'Robot', left: bool, right: bool):
        if len(self.route.path) != 0:
            if self.current_MRT_line == MRTLine.EWL:
                if left:
                    train.steer_left()
                elif right:
                    train.steer_right()
        else:
            train.stop()

    def on_yellow(self, train: 'Robot', left: bool, right: bool):
        if len(self.route.path) != 0:
            if self.current_MRT_line == MRTLine.CCL:
                if left:
                    train.steer_left()
                elif right:
                    train.steer_right()
        else:
            train.stop()

    def on_red(self, train: 'Robot', left: bool, right: bool):
        if len(self.route.path) != 0:
            if self.current_MRT_line == MRTLine.NSL:
                if left:
                    train.steer_left()
                elif right:
                    train.steer_right()
        else:
            train.stop()

    def on_white(self, train: 'Robot', left: bool, right: bool):
        if len(self.route.path) != 0:
            if left and right:
                train.move_forward()

    def on_brown(self, train: 'Robot', left: bool, right: bool):
        if len(self.route.path) != 0:
            train.move_forward()
        else:
            train.stop()

    def on_click(self, train: 'Robot'):
        if len(self.route.path) != 0:
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

    def add_listener(self, listener: 'DriverListener'):
        self.listeners.append(listener)

class DriverListener(object):
    def on_station_reached(self, station: 'Station', line: 'Line'):
        pass

    def on_line_change(self, station: 'Station', curr_line: 'Line', target_line: 'Line'):
        pass

    def on_end_station_reached(self, station: 'Station', line: 'Line'):
        pass