from ev3dev.ev3 import ColorSensor, LargeMotor, TouchSensor
from utils.color import Color

STEERING_POWER = 500
TURNING_POWER = 1000
DEFAULT_POWER = 250

class Train(object):
    def __init__(self):
        self.left_color_sensor = ColorSensor('in4')
        self.right_color_sensor = ColorSensor('in1')
        self.left_large_motor = LargeMotor('outD')
        self.right_large_motor = LargeMotor('outA')
        self.touch_sensor = TouchSensor('in3')
        self.listeners = []
        self.prev_is_pressed = False

    def move_forward(self):
        self.left_large_motor.run_forever(speed_sp=DEFAULT_POWER)
        self.right_large_motor.run_forever(speed_sp=DEFAULT_POWER)

    def move_backward(self):
        self.left_large_motor.run_forever(speed_sp=-DEFAULT_POWER)
        self.right_large_motor.run_forever(speed_sp=-DEFAULT_POWER)

    def steer_left(self):
        self.left_large_motor.run_forever(speed_sp=DEFAULT_POWER)
        self.right_large_motor.run_forever(speed_sp=STEERING_POWER)

    def steer_right(self):
        self.left_large_motor.run_forever(speed_sp=STEERING_POWER)
        self.right_large_motor.run_forever(speed_sp=DEFAULT_POWER)

    def turn_left(self):
        self.left_large_motor.run_forever(speed_sp=TURNING_POWER)
        self.right_large_motor.run_forever(speed_sp=-TURNING_POWER)

    def turn_right(self):
        self.left_large_motor.run_forever(speed_sp=-TURNING_POWER)
        self.right_large_motor.run_forever(speed_sp=TURNING_POWER)

    def stop(self):
        self.left_large_motor.stop()
        self.right_large_motor.stop()

    def step(self):
        left_color = self.left_color_sensor.color
        right_color = self.right_color_sensor.color

        if left_color == Color.BLACK or right_color == Color.BLACK:
            for listener in self.listeners:
                listener.on_black(self, left_color == Color.BLACK, right_color == Color.BLACK)

        if left_color == Color.BLUE or right_color == Color.BLUE:
            for listener in self.listeners:
                listener.on_blue(self, left_color == Color.BLUE, right_color == Color.BLUE)

        if left_color == Color.GREEN or right_color == Color.GREEN:
            for listener in self.listeners:
                listener.on_green(self, left_color == Color.GREEN, right_color == Color.GREEN)

        if left_color == Color.YELLOW or right_color == Color.YELLOW:
            for listener in self.listener:
                listener.on_yellow(self, left_color == Color.YELLOW, right_color == Color.YELLOW)

        if left_color == Color.RED or right_color == Color.RED:
            for listener in self.listeners:
                listener.on_red(self, left_color == Color.RED, right_color == Color.RED)

        if left_color == Color.WHITE or right_color == Color.WHITE:
            for listener in self.listeners:
                listener.on_white(self, left_color == Color.WHITE, right_color == Color.WHITE)

        if left_color == Color.BROWN or right_color == Color.BROWN:
            for listener in self.listeners:
                listener.on_brown(self, left_color == Color.BROWN, right_color == Color.BROWN)

        if self.prev_is_pressed and not self.touch_sensor.is_pressed:
            for listener in self.listeners:
                listener.on_click(self)

        self.prev_is_pressed = self.touch_sensor.is_pressed

    def add_listener(self, listener: 'TrainListener'):
        self.listeners.append(listener)

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

    def on_click(self, train: 'Train'):
        pass
