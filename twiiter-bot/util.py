
from typing import NamedTuple


class SpeedData(NamedTuple):
    promised_down:int
    promised_up: int
    actuall_up: int
    actuall_down: int
