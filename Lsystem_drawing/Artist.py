import math


class Artist:
    """drawing_dataを解読してカメを操作する"""
    def __init__(self, kame, func_dict):
        self.func_dict = {i: (j[0], float(j[1:])) for i, j in func_dict.items()}
        self.kame = kame
        self.funcs = {}

    def process_f(self, arg):
        self.kame.forward(arg)

    def process_r(self, arg):
        self.kame.right(math.radians(arg))

    def process_l(self, arg):
        self.kame.left(math.radians(arg))

    def move_kame(self, sentence):
        for c in sentence:
            try:
                func_ = self.func_dict[c]
            except KeyError:
                raise DrawFuncsError("処理が定義されていない文字：" + c)
            if func_[0] == "f":
                self.process_f(func_[1])
            elif func_[0] == "r":
                self.process_r(func_[1])
            elif func_[0] == "l":
                self.process_l(func_[1])
            else:
                raise DrawFuncsError("無効な処理：" + func_[0] + func_[1])


class DrawFuncsError(Exception):
    pass
