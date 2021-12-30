import math
from PIL import Image, ImageDraw

from Lsystem_drawing.Integrator import Integrator


def main():
    integ = Integrator(
        Omega="a",
        P={
            "a": "lararal",
            "b": "ab"
            },
        DrawFuncs={
               "a": ("f", 500),
               "b": ("r", 30),
               "r": ("r", 108),
               "l": ("l", 72),
           },
        Round=7
                        )
    integ.draw()
    integ.save("pictures/integ_test.png")

if __name__ == '__main__':
    main()