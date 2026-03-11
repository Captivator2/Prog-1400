from .tile_type import TileType
from .position import Position
from .movement import move_position

class TileMap:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def in_bounds(self, pos):
        return 0 <= pos.row < self.rows and 0 <= pos.col < self.cols

    def get_tile(self, pos):
        if not self.in_bounds(pos):
            return TileType.WALL
        return self.grid[pos.row][pos.col]

    def is_walkable(self, pos):
        tile = self.get_tile(pos)
        return tile != TileType.WALL


if __name__ == "__main__":
    grid = [
        [TileType.WALL, TileType.WALL, TileType.WALL],
        [TileType.WALL, TileType.PATH, TileType.WALL],
        [TileType.WALL, TileType.PATH, TileType.WALL],
        [TileType.WALL, TileType.WALL, TileType.WALL],
    ]

    world = TileMap(grid)

    print(world.is_walkable(Position(1, 1)))  # True
    print(world.is_walkable(Position(0, 0)))  # False
    print(world.is_walkable(Position(5, 5)))  # False

    player_pos = Position(1, 1)
    print("Start:", player_pos)

    while True:
        direction = input("Move (w/a/s/d) or q to quit: ").lower()

        if direction == "q":
            break

        new_pos = move_position(player_pos, direction)

        if world.is_walkable(new_pos):
            player_pos = new_pos
            print("Moved to:", player_pos)
        else:
            print("Blocked")