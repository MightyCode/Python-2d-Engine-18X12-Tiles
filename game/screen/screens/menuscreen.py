# Class to display the main game menu

from game.inputs.inputmanager import InputManager as im
from game.screen.screens import screen
from game.render.text import text
from game.render.gui import button


class MenuScreen(screen.Screen):

    def __init__(self, info):
        super().__init__()

        self.title = text.Text("pixel1")
        self.title.setAll("Moteur de base", 1, [9, 10], [0.5, 0, 0.3, 1], "")

        self.copyleft = text.Text("pixel1")
        self.copyleft.setAll("(Copyleft) 2019 Maxence & Alexandre" + " " * 27, 0.4, [0, 0], [1, 1, 1, 1], "down-left")

        self.version = text.Text("pixel1")
        self.version.setAll("v.0.0.0.1", 0.4, [18, 0], [1, 1, 1, 1], "down-right")

        self.credits = text.Text("pixel1")
        self.credits.setAll("Maxence Bazin\nAlexandre Boin", 0.45, [9, 4.7], [1, 1, 1, 1], "")

        self.showCredits = False

        def gameLocal():
            from game.screen import gamemanager
            gamemanager.GameManager.setCurrentScreen("gamescreen", [False])

        def gameQuit():
            from game.main.window import Window
            Window.exit()

        def toggleCredits(): self.showCredits ^= True

        self.playLocal = button.Button([9, 5.9], [5, 1], "Jouer ;-)", gameLocal)

        self.showCreditsBtn = button.Button([7.7, 3.3], [2.45, 0.6], "Crédits", toggleCredits)

        self.hideCreditsBtn = button.Button([7.7, 3.3], [2.45, 0.6], "< Retour", toggleCredits)

        self.quit = button.Button([10.3, 3.3], [2.45, 0.6], "Quitter", gameQuit)

    def update(self):
        # Exit test
        if im.inputPressed(im.ESCAPE):
            from game.main.window import Window
            Window.exit()

        # Update buttons
        self.playLocal.update()
        if self.showCredits:
            self.hideCreditsBtn.update()
        else:
            self.showCreditsBtn.update()
        self.quit.update()

    def display(self):
        self.title.display()
        self.copyleft.display()
        self.version.display()
        self.quit.display()

        if self.showCredits:
            self.credits.display()
            self.hideCreditsBtn.display()
        else:
            self.playLocal.display()
            self.showCreditsBtn.display()

    def unload(self):
        self.title.unload()
        self.copyleft.unload()
        self.version.unload()
        self.playLocal.unload()
        self.showCreditsBtn.unload()
        self.hideCreditsBtn.unload()
        self.quit.unload()
