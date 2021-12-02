from Lsystem_drawing.Artist import Artist,Artist_rad
from Lsystem_drawing.Kame import Kame
from Lsystem_drawing.Lsystem import Lsystem

class Integrator:
    def __init__(self,drawing_data,bg_color=(255,255,255),line_color=(0,0,0),size=500):
        self.kame = Kame(canvas_size=size)
        self.kame.set_bg_color(bg_color)
        self.kame.set_line_color(line_color)
        self.ls = Lsystem(drawing_data.Omega, drawing_data.P)
        self.artist = Artist(self.kame, drawing_data.DrawFuncs)
        self.round = drawing_data.round

    def draw(self,show=False):
        self.ls.derive(self.round)
        self.artist.move(self.ls.pop_state())
        self.kame.draw(show=show)

    def save(self,filename):
        self.kame.save(filename)

    def set_bg_color(self,bg_color):
        self.kame.set_bg_color(bg_color)

    def set_line_color(self,line_color):
        self.kame.set_line_color(line_color)

    def set_canvas_size(self,size):
        self.kame.set_canvas_size(size)

    def get_image(self):
        return self.kame.image.copy()

    def pop_image(self):
        return self.kame.pop_image()

