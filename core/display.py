import numpy as np


class Frame:
    def __init__(self, **kwargs) -> None:
        self.array = kwargs.get('frame', np.empty([*kwargs['shape'], 3], dtype=int))

    def point(y: int, x: int, rgba: list) -> None:
        pass



class Screen:

    def __init__(self, **kwargs) -> None:
        self.shape = kwargs['shape'] # (H, W)
        self.lib = kwargs['lib']
        self.frame = kwargs.get('frame', Frame(shape=self.shape))

    def get_frame(self,) -> Frame:
        return self.frame

    def push_frame(self,) -> None:
        pass



