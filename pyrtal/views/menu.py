from random import randint

import arcade

from pyrtal.lib.utils import clamp


class MenuItem:
    DUNCAN = MIN = 0
    NATALIE = 1
    QUIT = MAX = 2


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.selected = 0
        self.jiggle = 8

    def on_show(self):
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Pyrtal", self.window.width / 2, self.window.height - 260, arcade.color.DUKE_BLUE, 96, anchor_x="center", bold=True)
        arcade.draw_text(
            "Duncan",
            self.window.width / 2 + (randint(-self.jiggle, self.jiggle) if self.selected == MenuItem.DUNCAN else 0),
            self.window.height - 520 + (randint(-self.jiggle, self.jiggle) if self.selected == MenuItem.DUNCAN else 0),
            arcade.color.DUKE_BLUE,
            48,
            anchor_x="center"
        )
        arcade.draw_text(
            "Natalie",
            self.window.width / 2 + (randint(-self.jiggle, self.jiggle) if self.selected == MenuItem.NATALIE else 0),
            self.window.height - 600 + (randint(-self.jiggle, self.jiggle) if self.selected == MenuItem.NATALIE else 0),
            arcade.color.DUKE_BLUE,
            48,
            anchor_x="center"
        )
        arcade.draw_text(
            "Quit",
            self.window.width / 2 + (randint(-self.jiggle, self.jiggle) if self.selected == MenuItem.QUIT else 0),
            self.window.height - 680 + (randint(-self.jiggle, self.jiggle) if self.selected == MenuItem.QUIT else 0),
            arcade.color.DUKE_BLUE,
            48,
            anchor_x="center"
        )

    def on_key_press(self, symbol: int, modifiers: int):
        super().on_key_press(symbol, modifiers)

        # python arcade doesn't work with 3.10, yet
        # match symbol:
        #     case arcade.key.DOWN:
        #         self.selected = clamp(MIN_MENU, self.selected + 1, MAX_MENU)
        #     case arcade.key.UP:
        #         self.selected = clamp(MIN_MENU, self.selected - 1, MAX_MENU)

        if symbol == arcade.key.DOWN:
            self.selected = clamp(MenuItem.MIN, self.selected + 1, MenuItem.MAX)
        elif symbol == arcade.key.UP:
            self.selected = clamp(MenuItem.MIN, self.selected - 1, MenuItem.MAX)
        elif symbol == arcade.key.ENTER:
            if self.selected == MenuItem.DUNCAN:
                self.window.duncan_view.setup()
                self.window.show_view(self.window.duncan_view)
            elif self.selected == MenuItem.NATALIE:
                self.window.natalie_view.setup()
                self.window.show_view(self.window.natalie_view)
            elif self.selected == MenuItem.QUIT:
                arcade.exit()
        elif symbol == arcade.key.MINUS:
            self.jiggle = clamp(1, self.jiggle - 1, 20)
        elif symbol == arcade.key.EQUAL:
            self.jiggle = clamp(1, self.jiggle + 1, 20)

    def setup(self):
        self.selected = 0
        self.jiggle = 8
