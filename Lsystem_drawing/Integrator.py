from Lsystem_drawing.Artist import Artist
from Lsystem_drawing.Kame import Kame
from Lsystem_drawing.Lsystem import Lsystem

class Integrator:
    def __init__(self,
                 Omega,
                 P,
                 DrawFuncs,
                 Round,
                 bg_color=(255,255,255),
                 line_color=(0,0,0),
                 size=500,
                 angle_mode="d"):
        self.kame = Kame(canvas_size=size)
        self.kame.set_bg_color(bg_color)
        self.kame.set_line_color(line_color)

        self.ls = Lsystem(Omega, P)
        self.artist = Artist(self.kame, DrawFuncs,angle_mode=angle_mode)
        self.round = Round

    def draw(self,show=False,initialize=False):
        if initialize:
            self.ls.state = self.ls.Omega
            self.kame.reset()

        self.ls.derive(self.round)
        self.artist.move_kame(self.ls.get_state())
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


