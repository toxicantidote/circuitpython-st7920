"""Implementation of screen.Screen which writes the information to a Pillow Image"""

import sys
sys.path.append('../bitfont/python')
import canvas

from faces.font_5x7 import font

from PIL import Image,ImageDraw

import pyglet
from pyglet.gl import *

pilWhite = (255, 255, 255)
pilBlack = (0, 0, 0)

defaultWidth = 128
defaultHeight = 64

pilImageType = "RGB"
pilImagePitch = defaultWidth * -3

pygletScale = 8

class PillowScreen(canvas.Canvas):

    def __init__(self, x=0, y=0, scale=pygletScale):
        self.pilImage = Image.new(pilImageType, (defaultWidth, defaultHeight), color=pilWhite)
        self.pilDraw = ImageDraw.Draw(self.pilImage)
        self.pixelMap = self.pilImage.load()
        self.pygletImage = pyglet.image.ImageData(
            width=defaultWidth,
            height=defaultHeight,
            format=pilImageType,
            data=self.pilImage.tobytes(),
            pitch=pilImagePitch
        )
        self.pygletSprite = pyglet.sprite.Sprite(self.pygletImage, x, y)
        self.pygletSprite.scale = scale

    def plot(self, x, y, color=pilBlack):
        self.pixelMap[x,y] = color

    def clear(self):
        self.pilDraw.rectangle((0, 0, self.pilImage.width, self.pilImage.height), fill=pilWhite)

    def redraw(self):
        self.pygletImage.set_data(pilImageType, pilImagePitch, self.pilImage.tobytes())
        self.pygletSprite.image = self.pygletImage # force sprite to reload image

    def normalise_color(self, color):
        color = super().normalise_color(color)
        return pilWhite if color is 1 else pilBlack

if __name__ == "__main__":

    window = pyglet.window.Window(width=1024, height=512)

    smallFont = font
    bigFont = font
    screen = PillowScreen()
    blackPlotter = screen.create_plotter(canvas.black)
    whitePlotter = screen.create_plotter(canvas.white)

    screen.clear()
    font.draw_line("Hello World", blackPlotter)
    screen.redraw()

    @window.event
    def on_draw():
        pyglet.gl.glClearColor(255,255,255,255)
        # assists with scaling textures in expected (blocky) way, following https://gamedev.stackexchange.com/questions/20297/how-can-i-resize-pixel-art-in-pyglet-without-making-it-blurry
        glEnable(GL_TEXTURE_2D)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        window.clear()
        screen.pygletSprite.draw()

    pyglet.app.run()