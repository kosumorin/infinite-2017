from railway.station import Station
from railway.line import Line, MRTLine
from vehicle.robot import Robot, RobotListener
from utils.direction import MovementDirection

class Driver(RobotListener):
    def __init__(self):
        self.route = None
        self.current_MRT_line = None
        self.listeners = []

    def set_route(self, route: 'Route'):
        self.route = route
        self.current_MRT_line = route.start_line

    def clear_route(self):
        self.route = None
        self.current_MRT_line = None

    def on_invalid(self, train: 'Robot', left: bool, right: bool):
        if self.route is None:
            train.stop()
            return

        if len(self.route.path) == 0:
            train.stop()
        else:
            train.move_forward()

    def on_black(self, train: 'Robot', left: bool, right: bool):
        if self.route is None:
            train.stop()
            return

        if len(self.route.path) == 0:
            train.stop()
        else:
            train.move_forward()

    def on_blue(self, train: 'Robot', left: bool, right: bool):
        if self.route is None:
            train.stop()
            return

        if len(self.route.path) == 0:
            train.stop()
        else:
            train.move_forward()

    def on_green(self, train: 'Robot', left: bool, right: bool):
        if self.route is None:
            train.stop()
            return

        if len(self.route.path) == 0:
            train.stop()
        else:
            if self.current_MRT_line == MRTLine.EWL:
                if left:
                    train.steer_left()
                elif right:
                    train.steer_right()

    def on_yellow(self, train: 'Robot', left: bool, right: bool):
        if self.route is None:
            train.stop()
            return

        if len(self.route.path) == 0:
            train.stop()
        else:
            if self.current_MRT_line == MRTLine.CCL:
                if left:
                    train.steer_left()
                elif right:
                    train.steer_right()

    def on_red(self, train: 'Robot', left: bool, right: bool):
        if self.route is None:
            train.stop()
            return

        if len(self.route.path) == 0:
            train.stop()
        else:
            if self.current_MRT_line == MRTLine.NSL:
                if left:
                    train.steer_left()
                elif right:
                    train.steer_right()

    def on_white(self, train: 'Robot', left: bool, right: bool):
        if self.route is None:
            train.stop()
            return

        if len(self.route.path) == 0:
            train.stop()
        else:
            if left and right:
                train.move_forward()

    def on_brown(self, train: 'Robot', left: bool, right: bool):
        if self.route is None:
            train.stop()
            return

        if len(self.route.path) == 0:
            train.stop()
        else:
            train.move_forward()

    def on_click(self, train: 'Robot'):
        # Return function if there is route is None. If it is not None but has no more station path, return also.
        if self.route is None:
            return
        elif len(self.route.path) == 0:
            return

        station = self.route.path.pop(0)

        for listener in self.listeners:
            listener.on_station_reached(station, self.current_MRT_line)

        if station == self.route.end_station:
            train.stop()

            for listener in self.listeners:
                listener.on_end_station_reached(station, self.current_MRT_line)

        elif station == self.route.transfer_station:
            if self.route.transfer_turn_direction == MovementDirection.LEFT:
                train.turn_left()
            elif self.route.transfer_turn_direction == MovementDirection.RIGHT:
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