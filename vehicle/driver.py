from railway.station import Station
from railway.line import Line
from vehicle.robot import Robot, RobotListener
from utils.direction import MovementDirection
from utils.color import Color

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

    def on_invalid(self, robot: 'Robot', left: bool, right: bool):
        if self.route is None:
            robot.stop()
            return

        if len(self.route.station_path) == 0:
            robot.stop()
        else:
            robot.move_forward()

    def on_black(self, robot: 'Robot', left: bool, right: bool):
        if self.route is None:
            robot.stop()
            return

        if len(self.route.station_path) == 0:
            robot.stop()
        else:
            robot.move_forward()

    def on_blue(self, robot: 'Robot', left: bool, right: bool):
        if self.route is None:
            robot.stop()
            return

        if len(self.route.station_path) == 0:
            robot.stop()
        else:
            robot.move_forward()

    def on_green(self, robot: 'Robot', left: bool, right: bool):
        if self.route is None:
            robot.stop()
            return

        if len(self.route.station_path) == 0:
            robot.stop()
        else:
            if self.current_MRT_line.color == Color.GREEN:
                if left:
                    robot.steer_left()
                elif right:
                    robot.steer_right()

    def on_yellow(self, robot: 'Robot', left: bool, right: bool):
        if self.route is None:
            robot.stop()
            return

        if len(self.route.station_path) == 0:
            robot.stop()
        else:
            if self.current_MRT_line.color == Color.YELLOW:
                if left:
                    robot.steer_left()
                elif right:
                    robot.steer_right()

    def on_red(self, robot: 'Robot', left: bool, right: bool):
        if self.route is None:
            robot.stop()
            return

        if len(self.route.station_path) == 0:
            robot.stop()
        else:
            if self.current_MRT_line.color == Color.RED:
                if left:
                    robot.steer_left()
                elif right:
                    robot.steer_right()

    def on_white(self, robot: 'Robot', left: bool, right: bool):
        if self.route is None:
            robot.stop()
            return

        if len(self.route.station_path) == 0:
            robot.stop()
        else:
            if left and right:
                robot.move_forward()

    def on_brown(self, robot: 'Robot', left: bool, right: bool):
        if self.route is None:
            robot.stop()
            return

        if len(self.route.station_path) == 0:
            robot.stop()
        else:
            robot.move_forward()

    def on_click(self, robot: 'Robot'):
        # Return function if there is route is None. If it is not None but has no more station path, return also.
        if self.route is None:
            return
        elif len(self.route.station_path) == 0:
            return

        # Get station reached
        station = self.route.station_path.pop(0)

        # Alert all listeners
        for listener in self.listeners:
            listener.on_station_reached(station, self.current_MRT_line)

        # If station is destination, stop train & return function
        if station == self.route.end_station:
            robot.stop()

            # Alert listeners when reached end station
            for listener in self.listeners:
                listener.on_end_station_reached(station, self.current_MRT_line)

            return

        # If station is transfer station, alert all listeners
        if station == self.route.transfer_station:
            for listener in self.listeners:
                listener.on_line_change(station, self.current_MRT_line, self.route.end_line)

            self.current_MRT_line = self.route.end_line

        # Get movement direction to the next station.
        movement_direction = self.route.movement_flow.pop(0)

        # If next station is left or right, then turn left and right.
        if movement_direction == MovementDirection.LEFT:
            robot.turn_left()
        elif movement_direction == MovementDirection.RIGHT:
            robot.turn_right()

        # Continue moving forward after turning. If next station is straight, move forward.
        robot.move_forward()

    def add_listener(self, listener: 'DriverListener'):
        self.listeners.append(listener)

class DriverListener(object):
    def on_station_reached(self, station: 'Station', line: 'Line'):
        pass

    def on_line_change(self, station: 'Station', curr_line: 'Line', target_line: 'Line'):
        pass

    def on_end_station_reached(self, station: 'Station', line: 'Line'):
        pass