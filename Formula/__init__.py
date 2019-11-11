import machine
import pyb
from Formula.views import HomeView

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

    def incr_timer(self) -> None:
        self.timer += 1

    def update(self) -> None:
        self.interaction.extend(*self.get_touch())
        while len(self.interaction) >= 1:
            self.timer = 0
            self.interact(self.view[-1], self.interaction.pop())
        

    def sleep(self) -> None:
        self.interaction.extend(*self.get_gesture())
        while len(self.interaction):
            if self.interaction.pop().g_force > 1:
                return True
