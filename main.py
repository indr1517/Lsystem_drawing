import math
from PIL import Image, ImageDraw

from Lsystem_drawing.Artist import Artist
from Lsystem_drawing.Kame import Kame
from drawing_source import pattern1
from Lsystem_drawing.Lsystem import Lsystem
from Lsystem_drawing.Integrator import Integrator

"""
Lsystemによる文の生成/条件の設定
文解釈の設定
描画/描画設定（色、線の太さ、画像サイズ）
PNG出力
画像の結合

開始記号、生成規則、ラウンド数
↓
文
↓　　←記号の解釈
線の集合
↓　　←背景、線の色、太さ、画素数、（縦横比、中心の位置、線のピクセル長さ）
Pillow Imageオブジェクト
↓　　←結合（しない、一次元縦横、二次元）
PNGファイル


初期化して描画
"""

def main():
    integ = Integrator(drawing_data=pattern1)

    imgs = []
    for round in range(10):
        integ.round = round
        integ.draw(initialize=True)

        imgs.append(integ.get_image())

    connect_vert(imgs).save("pictures/imgmat1.png")

def main_iter():
    drawing_data = pattern1
    kame = Kame(canvas_size=500)
    kame.set_line_color((255, 255, 255))
    kame.set_bg_color((0, 0, 0))
    ls = Lsystem(drawing_data.Omega, drawing_data.P)
    artist = Artist_rad(kame, drawing_data.DrawFuncs)

    imgs = [[] for _ in range(3, 16)]
    for angle in range(3, 16):
        for round in range(8):
            ls.derive(round)

            artist.func_dict["r"] = ("r", math.pi * (1 - 2 / angle))
            artist.func_dict["l"] = ("l", math.pi * (2 / angle))

            artist.move_kame(ls.pop_state())
            kame.draw()

            imgs[angle - 3].append(kame.pop_image())
    connect_mat(imgs).save("pictures/imgmat1.png")


if __name__ == '__main__':
    main()