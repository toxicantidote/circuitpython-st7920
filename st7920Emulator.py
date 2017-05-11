"""Implementation of screen.Screen which writes the information to a Pillow Image"""

import sys
from threading import Thread
import canvas
from time import sleep

from faces.font_5x7 import font

from PIL import Image,ImageDraw

import pyglet
from pyglet.gl import *

pilWhite = (255, 255, 255)
pilBlack = (0, 0, 0)
pilImageType = "RGB"
pilImagePitch = canvas.Canvas.width * -3

pygletImageFormat = "RGB"
pygletScale = 8

def noop(*a):
    pass

def createPygletWindow(pillowScreen):
    window = pyglet.window.Window(width=pillowScreen.width * pygletScale, height=pillowScreen.height * pygletScale)

    def refresh_window():
        pillowScreen.pygletImage.set_data(pygletImageFormat, pilImagePitch, pillowScreen.pilScreenImage.tobytes())
        pillowScreen.pygletSprite.image = pillowScreen.pygletImage
        # assists with scaling textures in expected (blocky) way,
        # following https://gamedev.stackexchange.com/questions/20297/how-can-i-resize-pixel-art-in-pyglet-without-making-it-blurry
        glEnable(GL_TEXTURE_2D)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        pillowScreen.pygletSprite.draw()

    #window.push_handlers(pyglet.window.event.WindowEventLogger())

    @window.event
    def on_expose():
        refresh_window()

    @window.event
    def on_draw():
        refresh_window()

    pyglet.clock.schedule_interval(noop, 0.1)

    return window

class PillowScreen(canvas.Canvas):

    def __init__(self, x=0, y=0, scale=pygletScale):
        # construct the buffer (equivalent to micropython in-memory buffer
        self.pilBufferImage = Image.new(pilImageType, (canvas.Canvas.width, canvas.Canvas.height), color=pilWhite)
        self.pilBufferDraw = ImageDraw.Draw(self.pilBufferImage) # exposes draw operations on buffer
        self.pixelMap = self.pilBufferImage.load() # used to buffer pixels for future drawing to screen

        # construct the screen (equivalent to the actual registers
        self.pilScreenImage = Image.new(pilImageType, (canvas.Canvas.width, canvas.Canvas.height), color=pilWhite)

        # image for painting screen using scaled pyglet sprites
        self.pygletImage = pyglet.image.ImageData(
            width=self.pilScreenImage.width,
            height=self.pilScreenImage.height,
            format=pygletImageFormat,
            data=self.pilScreenImage.tobytes(),
            pitch=pilImagePitch
        )
        self.pygletSprite = pyglet.sprite.Sprite(self.pygletImage, 0, 0)
        self.pygletSprite.scale = pygletScale

    def plot(self, x, y, set=False):
        if x >=0 and x < canvas.Canvas.width and y >= 0 and y < canvas.Canvas.height:
            self.pixelMap[x,y] = pilWhite if set else pilBlack
        else:
            pass

    def clear(self):
        self.pilBufferDraw.rectangle((0, 0, self.pilBufferImage.width, self.pilBufferImage.height), fill=pilWhite)

    def redraw(self, dx1=0, dy1=0, dx2=127, dy2=63):
        """
        assert 0 <= dx1 and dx1 < canvas.Canvas.width, "Bad coord"
        assert 0 <= dx2 and dx2 < canvas.Canvas.width, "Bad coord"
        assert 0 <= dy1 and dy1 < canvas.Canvas.height, "Bad coord"
        assert 0 <= dy2 and dy2 < canvas.Canvas.height, "Bad coord"
        """
        dx1 = max(0, dx1)
        dx2 = max(0, dx2)
        dy1 = max(0, dy1)
        dy2 = max(0, dy2)
        dx1 = min(canvas.Canvas.width - 1, dx1)
        dx2 = min(canvas.Canvas.width - 1, dx2)
        dy1 = min(canvas.Canvas.height - 1, dy1)
        dy2 = min(canvas.Canvas.height - 1, dy2)
        if dx1 is not dx2 and dy1 is not dy2:
            # create a cropped image for the redraw area
            # make a sprite and schedule a draw of this sprite
            box = (dx1, dy1, dx2 + 1, dy2 + 1)
            croppedPilImage = self.pilBufferImage.crop(box)
            self.pilScreenImage.paste(croppedPilImage, box)
        else:
            pass

    def normalise_color(self, color):
        color = super().normalise_color(color)
        return pilWhite if color is 1 else pilBlack

if __name__ == "__main__":

    smallFont = font
    bigFont = font
    screen = PillowScreen()
    blackPlotter = screen.create_plotter(canvas.black)
    whitePlotter = screen.create_plotter(canvas.white)

    createPygletWindow(screen)

    def draw_once(*a):
        print("Once")
        screen.clear()
        lineWidth = font.draw_line(b"Hello World", blackPlotter)
        screen.redraw(0,0, lineWidth, font.height)

    def draw_twice(*a):
        print("Twice")
        screen.clear()
        lineWidth = font.draw_line(b"Hello Mars", blackPlotter)
        screen.redraw(0,0, lineWidth, font.height)

    def loop():
        draw_once()
        draw_twice()

    thread = Thread(target=loop)
    thread.start()

    pyglet.app.run()