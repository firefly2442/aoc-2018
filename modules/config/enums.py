from enum import Enum

class Actions(Enum):
    NONE = 0
    WORKING = 1
    SLEEPING = 2
    WAKING = 3

class SleepState(Enum):
    NONE = 0
    AWAKE = 1
    ASLEEP = 2
