from enum import Enum, auto

class TurnDir(Enum):
    L = auto()
    R = auto()


class AccDir(Enum):
    FORWARD = auto()
    BACKWARD = auto()