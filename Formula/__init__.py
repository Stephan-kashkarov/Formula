import machine
import pyb
import ft6206 as touch
from lis2hh12 import accel
from views import HomeView

class Touch:
    def __init__(self, **kwargs):
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.id = kwargs['id']


class Gesture:
    def __init__(self, **kwargs):
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.z = kwargs['z']

    def total(self):
        return sum([abs(x) for x in [self.x, self.y, self.z]])

class App:
    def __init__(self):
        self.active = True
        self.spi = machine.SPI(1)
        self.i2c = machine.I2C(freq=400000)
        self.interaction = list()
        self.view = [HomeView()]
        self.timer = 0
        self.sleep_timer = pyb.Timer(1)
        self.sleep_timer.init(freq=1)
        self.sleep_timer.callback(self.incr_timer())
        self.screen = None

    def incr_timer(self) -> None:
        self.timer += 1

    def update(self) -> None:
        self.interaction.extend(*self.get_touch())
        while len(self.interaction) >= 1:
            self.timer = 0
            self.interact(self.view[-1], self.interaction.pop())
        if not self.screen:
            self.screen = self.view[-1].render()
        self.screen.interact(self.interaction.pop())
        self.screen.draw()
        

    def sleep(self) -> None:
        self.interaction.extend(*self.get_gesture())
        while len(self.interaction):
            if self.interaction.pop().total() > 256:
                return True

    def get_touch(self) -> [Touch]:
        for i in range(5):
            for event in touch.read():
                yield Touch(**event)

    def get_gesture(self) -> [Gesture]:
        for i in range(5):
            for event in accel.read():
                yield Gesture(**event)
