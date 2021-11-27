from Lsystem_drawing.Artist import Artist
from Lsystem_drawing.Kame import Kame
from drawing_source import pattern1
from Lsystem_drawing.Lsystem import Lsystem


def main():
    drawing_data = pattern1
    kame = Kame()
    ls = Lsystem(drawing_data.Omega, drawing_data.P)
    artist = Artist(drawing_data.DrawFuncs)

    ls.derive(drawing_data.Round)
    artist.move_kame(kame, ls.state)
    kame.draw()
    kame.save("pictures/img.png")


if __name__ == '__main__':
    main()