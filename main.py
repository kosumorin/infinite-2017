#!/usr/bin/env python3

from movement import Movement, MovementCallback
import line

# Change line here!
current_line = line.EWL

class BaseMovementCallback(MovementCallback):
    # TODO: STATIONS
    def on_black(self, movement_obj: 'Movement', left: bool, right: bool):
        pass

    # TODO: INTERSECTIONS
    def on_blue(self, movement_obj: 'Movement', left: bool, right: bool):
        pass

    def on_green(self, movement_obj: 'Movement', left: bool, right: bool):
        movement_obj.stop_movement()

    def on_yellow(self, movement_obj: 'Movement', left: bool, right: bool):
        movement_obj.stop_movement()

    def on_red(self, movement_obj: 'Movement', left: bool, right: bool):
        movement_obj.stop_movement()

    # Move forward on white
    def on_white(self, movement_obj: 'Movement', left: bool, right: bool):
        if left and right:
            movement_obj.forward_movement()

    def on_brown(self, movement_obj: 'Movement', left: bool, right: bool):
        movement_obj.stop_movement()

class EWLMovementCallback(BaseMovementCallback):
    def on_green(self, movement_obj: 'Movement', left: bool, right: bool):
        if left:
            movement_obj.left_movement()
        elif right:
            movement_obj.right_movement()

class NSLMovementCallback(BaseMovementCallback):
    def on_red(self, movement_obj: 'Movement', left: bool, right: bool):
        if left:
            movement_obj.left_movement()
        if right:
            movement_obj.right_movement()

class CCLMovementCallback(BaseMovementCallback):
    def on_yellow(self, movement_obj: 'Movement', left: bool, right: bool):
        if left:
            movement_obj.left_movement()
        elif right:
            movement_obj.right_movement()

if __name__ == "__main__":
    robot = Movement()

    while True:
        if current_line == line.EWL:
            robot.step(EWLMovementCallback)
        elif current_line == line.NSL:
            robot.step(NSLMovementCallback)
        elif current_line == line.CCL:
            robot.step(CCLMovementCallback)