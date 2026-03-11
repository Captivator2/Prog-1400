from .position import Position

def move_position(pos, direction):
    if direction == "w":
        return Position(pos.row - 1, pos.col)
    if direction == "s":
        return Position(pos.row + 1, pos.col)
    if direction == "a":
        return Position(pos.row, pos.col - 1)
    if direction == "d":
        return Position(pos.row, pos.col + 1)
    return pos