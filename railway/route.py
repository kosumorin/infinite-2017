from railway.station import Station, MRTStation
from railway.line import Line, MRTLine
from utils.direction import TrainDirection, Direction, MovementDirection

class Route(object):
    def __init__(self, start_station: 'Station', end_station: 'Station', start_line: 'Line', end_line: 'Line', transfer_station: 'Station' = None):
        self.start_station = start_station
        self.end_station = end_station
        self.start_line = start_line
        self.end_line = end_line
        self.transfer_station = transfer_station
        self.station_path = []
        self.movement_flow = []

        self.generate_path()

    def generate_path(self):
        if self.start_line != self.end_line:
            train_direction_start_line = self.get_train_direction(self.start_line, self.start_station, self.transfer_station)
            train_direction_end_line = self.get_train_direction(self.end_line, self.transfer_station, self.end_station)

            self.add_station_to_path(train_direction_start_line, self.start_line, self.start_station, self.transfer_station)
            self.add_station_to_path(train_direction_end_line, self.end_line, self.transfer_station, self.end_station)

            self.add_movement_to_path(train_direction_start_line, self.start_line, self.start_station, self.transfer_station)
            self.movement_flow.append(self.get_intersection_turn_direction(train_direction_start_line, train_direction_end_line))
            self.add_movement_to_path(train_direction_end_line, self.end_line, self.transfer_station, self.end_station)

        else:
            train_direction = self.get_train_direction(self.start_line, self.start_station, self.end_station)
            self.add_station_to_path(train_direction, self.start_line, self.start_station, self.end_station)
            self.add_movement_to_path(train_direction, self.start_line, self.start_station, self.end_station)

    def add_station_to_path(self, train_dir: 'TrainDirection', line: 'Line', from_station: 'Station', to_station: 'Station'):
        if train_dir == TrainDirection.TOWARDS:
            for i in range(line.get_station_index(from_station) + 1, line.get_station_index(to_station) + 1):
                self.station_path.append(line.stations[i])
        elif train_dir == TrainDirection.OPPOSITE:
            for i in range(line.get_station_index(from_station) - 1, line.get_station_index(to_station) - 1, -1):
                self.station_path.append(line.stations[i])

    def add_movement_to_path(self, train_dir: 'TrainDirection', line: 'Line', from_station: 'Station', to_station: 'Station'):
        directions = []

        if train_dir == TrainDirection.TOWARDS:
            for i in range(line.get_station_index(from_station), line.get_station_index(to_station)):
                directions.append(line.stations[i].station_flow[line.name]["next"])

        elif train_dir == TrainDirection.OPPOSITE:
            for i in range(line.get_station_index(from_station), line.get_station_index(to_station), -1):
                directions.append(line.stations[i].station_flow[line.name]["previous"])

        for i in range(0, len(directions)):
            if i + 1 == len(directions):
                break

            current = directions[i]
            next = directions[i + 1]

            movement_direction = Direction.get_movement_direction(current, next)

            self.movement_flow.append(movement_direction)

    @staticmethod
    def get_train_direction(line: 'Line', from_station: 'Station', to_station: 'Station') -> 'TrainDirection':
        if line.get_station_index(from_station) < line.get_station_index(to_station):
            return TrainDirection.TOWARDS
        else:
            return TrainDirection.OPPOSITE

    def get_intersection_turn_direction(self, train_dir_start: 'TrainDirection', train_dir_end: 'TrainDirection') -> 'MovementDirection':
        if self.transfer_station is None:
            return

        if train_dir_start == TrainDirection.TOWARDS:
            prev_station = self.start_line.stations[self.start_line.get_station_index(self.transfer_station) - 1]

            from_direction = prev_station.station_flow[self.start_line.name]["next"]

        else:
            prev_station = self.start_line.stations[self.start_line.get_station_index(self.transfer_station) + 1]

            from_direction = prev_station.station_flow[self.start_line.name]["previous"]

        if train_dir_end == TrainDirection.TOWARDS:
            to_direction = self.transfer_station.station_flow[self.end_line.name]["next"]
        else:
            to_direction = self.transfer_station.station_flow[self.end_line.name]["previous"]

        return Direction.get_movement_direction(from_direction, to_direction)
