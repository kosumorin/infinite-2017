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

    def forward_movement(self):
        self.left_large_motor.run_forever(speed_sp=DEFAULT_POWER)
        self.right_large_motor.run_forever(speed_sp=DEFAULT_POWER)

    def left_movement(self):
        self.left_large_motor.run_forever(speed_sp=DEFAULT_POWER)
        self.right_large_motor.run_forever(speed_sp=TURNING_POWER)

    def right_movement(self):
        self.left_large_motor.run_forever(speed_sp=TURNING_POWER)
        self.right_large_motor.run_forever(speed_sp=DEFAULT_POWER)

    def stop_movement(self):
        self.left_large_motor.stop()
        self.right_large_motor.stop()

    def step(self, movement_listener_obj: 'MovementListener'):
        left_color = self.left_color_sensor.color
        right_color = self.right_color_sensor.color

        if left_color == color.BLACK or right_color == color.BLACK:
            movement_listener_obj.on_black(self, left_color == color.BLACK, right_color == color.BLACK)

        if left_color == color.BLUE or right_color == color.BLUE:
            movement_listener_obj.on_blue(self, left_color == color.BLUE, right_color == color.BLUE)

        if left_color == color.GREEN or right_color == color.GREEN:
            movement_listener_obj.on_green(self, left_color == color.GREEN, right_color == color.GREEN)

        if left_color == color.YELLOW or right_color == color.YELLOW:
            movement_listener_obj.on_yellow(self, left_color == color.YELLOW, right_color == color.YELLOW)

        if left_color == color.RED or right_color == color.RED:
            movement_listener_obj.on_red(self, left_color == color.RED, right_color == color.RED)

        if left_color == color.WHITE or right_color == color.WHITE:
            movement_listener_obj.on_white(self, left_color == color.WHITE, right_color == color.WHITE)

        if left_color == color.BROWN or right_color == color.BROWN:
            movement_listener_obj.on_brown(self, left_color == color.BROWN, right_color == color.BROWN)

class TrainListener(object):
    def on_black(self, movement_obj: 'Movement', left: bool, right: bool):
        pass

    def on_blue(self, movement_obj: 'Movement', left: bool, right: bool):
        pass

    def on_green(self, movement_obj: 'Movement', left: bool, right: bool):
        pass

    def on_yellow(self, movement_obj: 'Movement', left: bool, right: bool):
        pass

    def on_red(self, movement_obj: 'Movement', left: bool, right: bool):
        pass

    def on_white(self, movement_obj: 'Movement', left: bool, right: bool):
        pass

    def on_brown(self, movement_obj: 'Movement', left: bool, right: bool):
        pass
