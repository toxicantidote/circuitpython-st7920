from PIL import Image,ImageDraw

class Screen():

    def __init__(self, width=128,height=64, imageType="l", color=1):
        self.image = Image.new(imageType, (width, height), color=color)
        self.pixelMap = self.image.load()
        def plot(x,y,white=false):
            self.pixelMap[x,y] = 1 if white else 0
        self.plot = plot

    def draw_para(self, para, font, x, y, drawWhite=False):
        font.draw_para(para, x, y, self.plot, drawWhite)

def run():
    from bitFont.faces.font_5x7 import font
    drawWhite = False
    message = "Hello World"
    (width, height) = font.para_dims(self, message)
    screen = Screen(width=width, height=height)
    font.draw_para(message, 0, 0, screen.plot, drawWhite)
    screen.image.save("message.png")

if __name__ == "__main__":
    run()