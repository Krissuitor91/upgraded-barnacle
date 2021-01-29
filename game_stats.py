class GameStats:

    def __init__(self, ai_game):
        """Initialise stats."""
        self.settings = ai_game.settings
        self.reset_stats()

        """Start game in an active state."""
        self.game_active = False

    def reset_stats(self):
        """Stats that can change during the game."""
        self.ships_left = self.settings.ship_limit