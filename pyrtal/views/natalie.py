import arcade


class NatalieView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show(self):
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Natalie", self.window.width / 2, self.window.height - 260, arcade.color.DUKE_BLUE, 96, anchor_x="center", bold=True)

    def on_key_press(self, symbol: int, modifiers: int):
        super().on_key_press(symbol, modifiers)

        if symbol == arcade.key.ESCAPE:
            self.window.menu_view.setup()
            self.window.show_view(self.window.menu_view)

    def setup(self):
        pass
