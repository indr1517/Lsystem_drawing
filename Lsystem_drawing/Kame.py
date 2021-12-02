import math

from PIL import Image, ImageDraw
# import copy


class Kame:
    """位置と向きを持って移動するエージェントを使って作図する。また図をpng形式で保存する"""
    def __init__(self,canvas_size=1000):
        self.pos = (0.0, 0.0)
        self.head = 0.0
        self.line_list = []
        self.canvas_size = (canvas_size, canvas_size)
        self.line_color = (0, 0, 0)
        self.bg_color = (255, 255, 255)

        self.image = Image.new("RGB", self.canvas_size, self.bg_color)
        self.draw_ = ImageDraw.Draw(self.image)

    def forward(self, distance):
        start = self.pos
        self.pos = (self.pos[0] + distance * math.cos(self.head),
                    self.pos[1] + distance * math.sin(self.head))
        self.line_list.append((start, self.pos))

    def left(self, rad):
        self.head += rad

    def right(self, rad):
        self.head -= rad

    def set_bg_color(self, color):
        self.bg_color = color
        self.draw_.rectangle((0,0,self.canvas_size[0],self.canvas_size[1]),fill=self.bg_color)
        # self.image = Image.new("RGB", self.canvas_size, self.bg_color)
        # self.draw_ = ImageDraw.Draw(self.image)

    def set_line_color(self, color):
        self.line_color = color

    def set_canvas_size(self,size):
        self.canvas_size = size
        self.image = Image.new("RGB", self.canvas_size, self.bg_color)
        self.draw_ = ImageDraw.Draw(self.image)

    def round_point(self, point, digit=0):
        if digit is None:
            return tuple([round(j) for j in point])
        else:
            return tuple([round(j, digit) for j in point])

    def get_line_set(self, digit=None):
        return set([
            tuple([
                self.round_point(point, digit)
                for point in line])
            for line in self.line_list])

    def get_point_set(self, digit=None):
        return set([self.round_point(k, digit)
                    for k in
                    [i for i, j in self.line_list]
                    + [self.line_list[-1][-1]]])

    def resize(self):
        x_max, y_max = map(max, zip(*self.get_point_set()))
        x_min, y_min = map(min, zip(*self.get_point_set()))
        center = ((x_max + x_min) / 2, (y_max + y_min) / 2)
        width_xy = x_max - x_min, y_max - y_min
        if width_xy[0] >= width_xy[1]:
            i = 0
            width = width_xy[0]
        else:
            i = 1
            width = width_xy[1]

        self.line_list = [
            tuple([
                ((point[0] - center[0]) * 0.9 * self.canvas_size[i] / width + self.canvas_size[0] / 2,
                 -(point[1] - center[1]) * 0.9 * self.canvas_size[i] / width + self.canvas_size[1] / 2)
                for point in line])
            for line in self.line_list
        ]

    def draw(self, show=False):
        if len(self.line_list) != 0:
            self.resize()

        for line in self.get_line_set():
            self.draw_.line(line, fill=self.line_color)
        if show:
            self.image.show()

    def save(self, filename):
        self.image.save(filename, quality=95)

    def reset(self):
        self.pos = (0.0, 0.0)
        self.head = 0.0
        self.line_list = []

        self.image = Image.new("RGB", self.canvas_size, self.bg_color)
        self.draw_ = ImageDraw.Draw(self.image)

    def pop_image(self):
        img = self.image.copy()
        self.reset()
        return img