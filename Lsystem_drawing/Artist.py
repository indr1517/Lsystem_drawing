import math


class Artist:
    """drawing_dataを解読してカメを操作する"""
    def __init__(self, kame, func_dict,angle_mode="d"):
        self.func_dict = func_dict
        self.kame = kame
        self.angle_mode = angle_mode

    def process_r(self, arg):
        if self.angle_mode == "d":
            self.kame.right(math.radians(arg))
        else:
            self.kame.right(arg)


    def process_l(self, arg):
        if self.angle_mode == "d":
            self.kame.left(math.radians(arg))
        else:
            self.kame.left(arg)


    def set_kame(self,kame):
        self.kame = kame

    def process_f(self, arg):
        self.kame.forward(arg)

    def set_angle_mode(self,angle_mode):
        self.angle_mode = angle_mode


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
                raise DrawFuncsError("無効な処理：" + func_[0] + str(func_[1]))


class DrawFuncsError(Exception):
    pass
