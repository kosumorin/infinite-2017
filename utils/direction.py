from enum import IntEnum

class TurnDirection(IntEnum):
    LEFT = 0
    RIGHT = 1

class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @classmethod
    def get_turn_direction(cls, from_dir: 'Direction', to_dir: 'Direction') -> 'TurnDirection':
        if from_dir == cls.NORTH:
            if to_dir == cls.EAST:
                return TurnDirection.RIGHT
            elif to_dir == cls.WEST:
                return TurnDirection.LEFT
        elif from_dir == cls.EAST:
            if to_dir == cls.SOUTH:
                return TurnDirection.RIGHT
            elif to_dir == cls.NORTH:
                return TurnDirection.LEFT
        elif from_dir == cls.SOUTH:
            if to_dir == cls.WEST:
                return TurnDirection.RIGHT
            elif to_dir == cls.EAST:
                return TurnDirection.LEFT
        elif from_dir == cls.WEST:
            if to_dir == cls.NORTH:
                return TurnDirection.RIGHT
            elif to_dir == cls.SOUTH:
                return TurnDirection.LEFT

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
