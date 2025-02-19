# local_planner.py
# ME 134 Team Penguinos
#
# Contains list of states

from enum import Enum

class State(Enum):
    FLOAT = 0
    PLAY = 1
    JOINT = 2
    CLAP = 3

    @classmethod
    def default(cls):
        return cls.FLOAT