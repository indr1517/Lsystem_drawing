import math
# import datetime
from PIL import Image, ImageDraw

from Lsystem_drawing.Integrator import Integrator
import Lsystem_drawing.Tools as lds

def main():
    integ = Integrator(
        Omega="a",
        P={
            "a": "larararal",
            "b": "ab"
            },
        DrawFuncs={
               "a": ("f", 500),
               "b": ("r", 30),
               "r": ("r", 108),
               "l": ("l", 72),
           },
        Round=7,
        bg_color=(0, 0, 0),
        line_color=(255, 255, 255),
        angle_mode="r"
                        )
    imgs = [[] for _ in range(3, 16)]
    for angle in range(3, 16):
        for round in range(8):
            integ.round = round
            integ.artist.func_dict["r"] = ("r", math.pi * (1 - 2 / angle))
            integ.artist.func_dict["l"] = ("l", math.pi * (2 / angle))

            integ.draw(initialize=True)
            imgs[angle - 3].append(integ.get_image())
    lds.save_img_list(imgs, f"pictures/img10.png", mode="m")

if __name__ == '__main__':
    main()