import pyglet
from pyglet.gl import *

# assists with scaling textures in expected (blocky) way, following https://gamedev.stackexchange.com/questions/20297/how-can-i-resize-pixel-art-in-pyglet-without-making-it-blurry
glEnable(GL_TEXTURE_2D)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

from bitFont.faces.font_5x7 import font

class Screen():

    def __init__(self):
        self.window = pyglet.window.Window(width=1024,height=512)

        def plot(x, y):
            pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                                 ('v2i', (x, self.window.height - y))
            )

        @self.window.event
        def on_draw():
            self.window.clear()
            dX = 1
            font.draw_text("Hello World", 1, 1, plot)

    def run(self):
        pyglet.app.run()