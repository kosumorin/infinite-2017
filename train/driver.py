from train.train import Train, TrainListener

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