import math
from PIL import Image, ImageDraw

from Lsystem_drawing.Artist import Artist,Artist_rad
from Lsystem_drawing.Kame import Kame
from drawing_source import pattern1
from Lsystem_drawing.Lsystem import Lsystem


def main():
    drawing_data = pattern1
    kame = Kame(canvas_size=500)
    ls = Lsystem(drawing_data.Omega, drawing_data.P)
    artist = Artist_rad(kame, drawing_data.DrawFuncs)
    ims = []
    for angle in range(3,13):
        ims2 = []
        for round in range(7):
            ls.set_Omega("al"*angle)
            ls.derive(round)

            artist.func_dict["r"] = ("r", math.pi*(1-2/angle))
            artist.func_dict["l"] = ("l", math.pi*(2/angle))

            artist.move_kame(ls.state)
            kame.draw(show=False)
            ims2.append(kame.image)
            # kame.save(f"pictures/img{round}.png")

            kame.__init__(canvas_size=500)
            # ls.set_Omega(drawing_data.Omega)
            artist.set_kame(kame)
        ims.append(connect(*ims2))
    connect_vert(*ims).save("pictures/img_merge.png")

def connect(*ims):
    dst = Image.new("RGB",(sum([im.width for im in ims]),ims[0].height))
    dst.paste(ims[0],(0,0))
    for i,im in enumerate(ims[1:]):
        dst.paste(im,(sum([im.width for im in ims[:i+1]]),0))

    return dst

def connect_vert(*ims):
    dst = Image.new("RGB", (ims[0].width,sum([im.height for im in ims])))
    dst.paste(ims[0], (0, 0))
    for i, im in enumerate(ims[1:]):
        dst.paste(im, (0, sum([im.height for im in ims[:i + 1]])))

    return dst



if __name__ == '__main__':
    main()