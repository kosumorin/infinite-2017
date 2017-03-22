from enum import IntEnum

class MovementDirection(IntEnum):
    STRAIGHT = 0
    LEFT = 1
    RIGHT = 2

class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @classmethod
    def get_move_direction(cls, from_dir: 'Direction', to_dir: 'Direction') -> 'MovementDirection':
        if from_dir == cls.NORTH:
            if to_dir == cls.EAST:
                return MovementDirection.RIGHT
            elif to_dir == cls.WEST:
                return MovementDirection.LEFT
        elif from_dir == cls.EAST:
            if to_dir == cls.SOUTH:
                return MovementDirection.RIGHT
            elif to_dir == cls.NORTH:
                return MovementDirection.LEFT
        elif from_dir == cls.SOUTH:
            if to_dir == cls.WEST:
                return MovementDirection.RIGHT
            elif to_dir == cls.EAST:
                return MovementDirection.LEFT
        elif from_dir == cls.WEST:
            if to_dir == cls.NORTH:
                return MovementDirection.RIGHT
            elif to_dir == cls.SOUTH:
                return MovementDirection.LEFT

    @classmethod
    def opposite(cls, dir: 'Direction') -> 'Direction':
        if dir == cls.NORTH:
            return cls.SOUTH
        elif dir == cls.EAST:
            return cls.WEST
        elif dir == cls.SOUTH:
            return cls.NORTH
        elif dir == cls.WEST:
            return cls.EAST


class TrainDirection(IntEnum):
    TOWARDS = 0
    OPPOSITE = 1
