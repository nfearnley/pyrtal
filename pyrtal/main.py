import arcade


class MyGame(arcade.Window):
    def __init__(self):
        SCREEN_WIDTH = 1920
        SCREEN_HEIGHT = 1080
        SCREEN_TITLE = "Pyrtal"
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
