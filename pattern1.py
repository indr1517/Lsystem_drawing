import math
from PIL import Image, ImageDraw

from Lsystem_drawing.Artist import Artist
from Lsystem_drawing.Kame import Kame
from drawing_source import pattern1
from Lsystem_drawing.Lsystem import Lsystem
from Lsystem_drawing.Integrator import Integrator


def main2():
    drawing_data = pattern1
    integ = Integrator(drawing_data=drawing_data)
    integ.draw()
    integ.save("pictures/integ_test.png")

if __name__ == '__main__':
    main2()