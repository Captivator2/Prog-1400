from src.world.tile_type import TileType
from src.world.tile_map import TileMap
from src.world.position import Position
from src.entities.player import Player

grid = [
    [TileType.WALL, TileType.WALL, TileType.WALL],
    [TileType.WALL, TileType.PATH, TileType.WALL],
    [TileType.WALL, TileType.PATH, TileType.WALL],
    [TileType.WALL, TileType.WALL, TileType.WALL],
]

world = TileMap(grid)
player = Player(Position(1, 1))

print("Start:", player.position)

player.try_move("DOWN", world)
print("After DOWN:", player.position)

player.try_move("LEFT", world)
print("After LEFT:", player.position)