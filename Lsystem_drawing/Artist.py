import math


class Artist:
    def __init__(self,func_dict):
        self.func_dict = {i: (j[0], float(j[1:])) for i, j in func_dict.items()}

    def move_kame(self,kame,sentence):
        for c in sentence:
            func_ = self.func_dict[c]
            if func_[0] == "f":
                kame.forward(func_[1])
            elif func_[0] == "r":
                kame.right(math.radians(func_[1]))
            elif func_[0] == "l":
                kame.left(math.radians(func_[1]))
            else:
                raise