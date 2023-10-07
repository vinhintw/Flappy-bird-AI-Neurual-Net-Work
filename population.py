import config
import player

class Population:
    def __init__(self):
        self.player = player.Player()
    
    def update_live_player(self):
        if self.player.alive:
            self.player.think()
            self.player.draw(config.window)
            self.player.update(config.ground)
