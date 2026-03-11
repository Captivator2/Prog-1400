from enum import Enum

class TileType(Enum):
    WALL = "#"
    PATH = "."
    START = "S"
    EXIT = "E"