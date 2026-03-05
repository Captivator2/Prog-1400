from enum import Enum, auto

class GameState(Enum):
    GAME_START = auto()
    PLAYING = auto()
    GAME_OVER = auto()
    WIN_STATE = auto()


class GameStateMachine:
    def __init__(self):
        self.state = GameState.GAME_START

    def set_state(self, new_state):
        print("STATE:", self.state.name, "->", new_state.name)
        self.state = new_state

    def start_game(self):
        if self.state == GameState.GAME_START:
            self.set_state(GameState.PLAYING)

    def defender_touches_player(self):
        if self.state == GameState.PLAYING:
            self.set_state(GameState.GAME_OVER)

    def all_items_collected(self):
        if self.state == GameState.PLAYING:
            self.set_state(GameState.WIN_STATE)

    def restart(self):
        if self.state == GameState.GAME_OVER or self.state == GameState.WIN_STATE:
            self.set_state(GameState.GAME_START)
        
    def update(self):
        if self.state == GameState.GAME_START:
            print("Game is starting...")
        elif self.state == GameState.PLAYING:
            print("Game is playing...")
        elif self.state == GameState.GAME_OVER:
            print("Game over...")
        elif self.state == GameState.WIN_STATE:
            print("You win!")
        
if __name__ == "__main__":
    gsm = GameStateMachine()

    gsm.update()
    gsm.start_game()
    gsm.update()

    gsm.defender_touches_player()
    gsm.update()

    gsm.restart()
    gsm.update()