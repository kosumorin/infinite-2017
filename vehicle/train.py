from vehicle.robot import Robot
from vehicle.driver import Driver, DriverListener
from railway.route import Route

from enum import IntEnum
from threading import Thread

class Train(DriverListener):
    class State(IntEnum):
        RUNNING = 0
        STOPPED = 1

    class TrainThread(Thread):
        def __init__(self, robot: 'Robot'):
            super().__init__()
            self.robot = robot
            self.is_running = False

        def run(self):
            self.is_running = True

            while self.is_running:
                self.robot.step()

        def stop(self):
            self.is_running = False

    def __init__(self):
        self.robot = Robot()
        self.driver = Driver()
        self.thread = None
        self.state = self.State.STOPPED

        self.robot.add_listener(self.driver)
        self.driver.add_listener(self)

    def start(self, route: 'Route') -> bool:
        if self.state == self.State.STOPPED:
            self.driver.set_route(route)

            self.thread = self.TrainThread(self.robot)
            self.thread.start()

            self.state = self.State.RUNNING

            return True
        else:
            return False

    def stop(self, is_immediate: bool):
        if is_immediate and self.state == self.State.RUNNING:
            self.driver.clear_route()

            self.thread.stop()
            self.thread = None

            self.state = self.State.STOPPED

    def on_end_station_reached(self, station: 'Station', line: 'Line'):
        self.stop(True)