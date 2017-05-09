white = "white"
black = "black"

def raiseError(*a, **k):
    raise NotImplementedError()

class Canvas:

    clear = raiseError
    plot = raiseError
    redraw = raiseError

    def normalise_color(self, color):
        if color == white:
            color = 1
        elif color == black:
            color = 0
        assert color == 0 or color == 1, "Unrecognised color specification"
        return color

    def create_plotter(self, color=black):
        color = self.normalise_color(color)
        def plot(x,y):
            self.plot(x,y,color)
        return plot

    def line(self, x1, y1, x2, y2, set=True):
        diffX = abs(x2 - x1)
        diffY = abs(y2 - y1)
        shiftX = 1 if (x1 < x2) else -1
        shiftY = 1 if (y1 < y2) else -1
        err = diffX - diffY
        drawn = False
        while not drawn:
            self.plot(x1, y1, set)
            if x1 == x2 and y1 == y2:
                drawn = True
                continue
            err2 = 2 * err
            if err2 > -diffY:
                err -= diffY
                x1 += shiftX
            if err2 < diffX:
                err += diffX
                y1 += shiftY

    def fill_rect(self, x1, y1, x2, y2, set=True):
        for y in range(y1, y2 + 1):
            self.line(x1, y, x2, y, set)

    def rect(self, x1, y1, x2, y2, set=True):
        self.line(x1, y1, x2, y1, set)
        self.line(x2, y1, x2, y2, set)
        self.line(x2, y2, x1, y2, set)
        self.line(x1, y2, x1, y1, set)