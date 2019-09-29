# Class to update/display the game 

from game.screen.screens import screen
from game.render.text import text
from game.render.gui import button


class GameScreen(screen.Screen):
    def __init__(self, info):
        super().__init__()

        self.title = text.Text("pixel1")
        self.title.setAll("Jeu en lui même", 1, [9, 10], [0.5, 0, 0.3, 1], "")

        def returnToMenu():
            from game.screen import gamemanager
            gamemanager.GameManager.setCurrentScreen("menuscreen", [False])

        self.returnMenu = button.Button([1.8, 11.5], [3, 0.75], "Retour au menu", returnToMenu)

    def update(self):
        # Update buttons
        self.returnMenu.update()

    def display(self):
        self.title.display()
        self.returnMenu.display()

    def unload(self):
        self.title.unload()
        self.returnMenu.unload()
