from ev3dev.ev3 import ColorSensor, LargeMotor
from utils import color

TURNING_POWER = 500
DEFAULT_POWER = 250

class Train(object):
    def __init__(self):
        self.left_color_sensor = ColorSensor('in4')
        self.right_color_sensor = ColorSensor('in1')
        self.left_large_motor = LargeMotor('outD')
        self.right_large_motor = LargeMotor('outA')
        self.listener = None

    def move_forward(self):
        self.left_large_motor.run_forever(speed_sp=DEFAULT_POWER)
        self.right_large_motor.run_forever(speed_sp=DEFAULT_POWER)

    def move_backward(self):
        self.left_large_motor.run_forever(speed_sp=-DEFAULT_POWER)
        self.right_large_motor.run_forever(speed_sp=-DEFAULT_POWER)

    def turn_left(self):
        self.left_large_motor.run_forever(speed_sp=DEFAULT_POWER)
        self.right_large_motor.run_forever(speed_sp=TURNING_POWER)

    def turn_right(self):
        self.left_large_motor.run_forever(speed_sp=TURNING_POWER)
        self.right_large_motor.run_forever(speed_sp=DEFAULT_POWER)

    def stop(self):
        self.left_large_motor.stop()
        self.right_large_motor.stop()

    def set_listener(self, train_listener: 'TrainListener'):
        self.listener = train_listener

    def step(self):
        left_color = self.left_color_sensor.color
        right_color = self.right_color_sensor.color

        if left_color == color.BLACK or right_color == color.BLACK:
            self.listener.on_black(self, left_color == color.BLACK, right_color == color.BLACK)

        if left_color == color.BLUE or right_color == color.BLUE:
            self.listener.on_blue(self, left_color == color.BLUE, right_color == color.BLUE)

        if left_color == color.GREEN or right_color == color.GREEN:
            self.listener.on_green(self, left_color == color.GREEN, right_color == color.GREEN)

        if left_color == color.YELLOW or right_color == color.YELLOW:
            self.listener.on_yellow(self, left_color == color.YELLOW, right_color == color.YELLOW)

        if left_color == color.RED or right_color == color.RED:
            self.listener.on_red(self, left_color == color.RED, right_color == color.RED)

        if left_color == color.WHITE or right_color == color.WHITE:
            self.listener.on_white(self, left_color == color.WHITE, right_color == color.WHITE)

        if left_color == color.BROWN or right_color == color.BROWN:
            self.listener.on_brown(self, left_color == color.BROWN, right_color == color.BROWN)

class TrainListener(object):
    def on_black(self, train: 'Train', left: bool, right: bool):
        pass

    def on_blue(self, train: 'Train', left: bool, right: bool):
        pass

    def on_green(self, train: 'Train', left: bool, right: bool):
        pass

    def on_yellow(self, train: 'Train', left: bool, right: bool):
        pass

    def on_red(self, train: 'Train', left: bool, right: bool):
        pass

    def on_white(self, train: 'Train', left: bool, right: bool):
        pass

    def on_brown(self, train: 'Train', left: bool, right: bool):
        pass
