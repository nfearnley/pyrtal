import arcade

from pyrtal.views.duncan import DuncanView
from pyrtal.views.natalie import NatalieView

from .views.menu import MenuView


SCREEN_WIDTH = 720
SCREEN_HEIGHT = 960
SCREEN_TITLE = "Pyrtal"


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.menu_view = MenuView()
        self.duncan_view = DuncanView()
        self.natalie_view = NatalieView()

    def setup(self):
        self.menu_view.setup()
        self.show_view(self.menu_view)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
