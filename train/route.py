from railway.station import Station, MRTStation
from railway.line import Line, MRTLine
from utils.direction import TrainDirection, Direction

class Route(object):
    def __init__(self, start_station: 'Station', end_station: 'Station', start_line: 'Line', end_line: 'Line', transfer_station: 'Station' = None):
        self.start_station = start_station
        self.end_station = end_station
        self.start_line = start_line
        self.end_line = end_line
        self.transfer_station = transfer_station
        self.transfer_turn_direction = None
        self.path = []

    def generate_path(self):
        if self.start_line != self.end_line:
            train_direction_start_line = self.get_train_direction(self.start_line, self.start_station, self.transfer_station)
            self.add_station_to_path(train_direction_start_line, self.start_line, self.start_station, self.transfer_station)

            train_direction_end_line = self.get_train_direction(self.end_line, self.transfer_station, self.end_station)
            self.add_station_to_path(train_direction_end_line, self.end_line, self.transfer_station, self.end_station)

            train_flow_start_line = self.get_train_flow(train_direction_start_line, self.start_line, self.transfer_station)
            train_flow_end_line = self.get_train_flow(train_direction_end_line, self.end_line, self.transfer_station)

            self.transfer_turn_direction = Direction.get_turn_direction(train_flow_start_line, train_flow_end_line)
        else:
            train_direction = self.get_train_direction(self.start_line, self.start_station, self.end_station)
            self.add_station_to_path(train_direction, self.start_line, self.start_station, self.end_station)

    def add_station_to_path(self, train_dir: 'TrainDirection', line: 'Line', from_station: 'Station', to_station: 'Station'):
        if train_dir == TrainDirection.TOWARDS:
            for i in range(line.get_station_index(from_station) + 1, line.get_station_index(to_station) + 1):
                self.path.append(line.stations[i])
        elif train_dir == TrainDirection.OPPOSITE:
            for i in range(line.get_station_index(from_station) - 1, line.get_station_index(to_station) - 1, -1):
                self.path.append(line.stations[i])

    @staticmethod
    def get_train_direction(line: 'Line', from_station: 'Station', to_station: 'Station') -> 'TrainDirection':
        if line.get_station_index(from_station) < line.get_station_index(to_station):
            return TrainDirection.TOWARDS
        else:
            return TrainDirection.OPPOSITE

    @staticmethod
    def get_train_flow(train_dir: 'TrainDirection', line: 'Line', station: 'Station'):
        if train_dir == TrainDirection.OPPOSITE:
            return Direction.opposite(station.line_flow[line])
        else:
            return station.line_flow[line]


if __name__ == "__main__":
    route1 = Route(MRTStation.HABOURFRONT, MRTStation.WOODLANDS, MRTLine.CCL, MRTLine.NSL, MRTStation.BISHAN)
    route1.generate_path()
    print("Stations: ")
    for station in route1.path :
        print(station.name)
    print("\n\nTransfer at: " + route1.transfer_station.name)
    print("Turn at: " + str(route1.transfer_turn_direction))
